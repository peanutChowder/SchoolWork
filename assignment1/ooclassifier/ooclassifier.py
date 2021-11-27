# Copyright 2020-2021 Paul Lu
#--------------------------------------------
#   Name: Jacob Feng
#   ID: 1591656
#   CMPUT 274, Fall 2021
#
#   Assignment #1: Object-Oriented Classifier
#-------------------------------------------- 
import sys
import copy     # for deepcopy()

Debug = False   # Sometimes, print for debugging.  Overridable on command line.
InputFilename = "file.input.txt"
TargetWords = [
        'outside', 'today', 'weather', 'raining', 'nice', 'rain', 'snow',
        'day', 'winter', 'cold', 'warm', 'snowing', 'out', 'hope', 'boots',
        'sunny', 'windy', 'coming', 'perfect', 'need', 'sun', 'on', 'was',
        '-40', 'jackets', 'wish', 'fog', 'pretty', 'summer'
        ]


def open_file(filename=InputFilename):
    try:
        f = open(filename, "r")
        return(f)
    except FileNotFoundError:
        # FileNotFoundError is subclass of OSError
        if Debug:
            print("File Not Found")
        return(sys.stdin)
    except OSError:
        if Debug:
            print("Other OS Error")
        return(sys.stdin)


def safe_input(f=None, prompt=""):
    try:
        # Case:  Stdin
        if f is sys.stdin or f is None:
            line = input(prompt)
        # Case:  From file
        else:
            assert not (f is None)
            assert (f is not None)
            line = f.readline()
            if Debug:
                print("readline: ", line, end='')
            if line == "":  # Check EOF before strip()
                if Debug:
                    print("EOF")
                return("", False)
        return(line.strip(), True)
    except EOFError:
        return("", False)


class C274:
    def __init__(self):
        self.type = str(self.__class__)
        return

    def __str__(self):
        return(self.type)

    def __repr__(self):
        s = "<%d> %s" % (id(self), self.type)
        return(s)


class ClassifyByTarget(C274):
    def __init__(self, lw=[]):
        super().__init__() # Call superclass
        # self.type = str(self.__class__)
        self.allWords = 0
        self.theCount = 0
        self.nonTarget = []
        self.set_target_words(lw)
        self.initTF()
        return

    def initTF(self):
        self.TP = 0
        self.FP = 0
        self.TN = 0
        self.FN = 0
        return

    # FIXME:  Incomplete.  Finish get_TF() and other getters/setters.
    def get_TF(self):
        return(self.TP, self.FP, self.TN, self.FN)

    # TODO: Could use Use Python properties
    #     https://www.python-course.eu/python3_properties.php
    def set_target_words(self, lw):
        # Could also do self.targetWords = lw.copy().  Thanks, TA Jason Cannon
        self.targetWords = copy.deepcopy(lw)
        return

    def get_target_words(self):
        return(self.targetWords)

    def get_allWords(self):
        return(self.allWords)

    def incr_allWords(self):
        self.allWords += 1
        return

    def get_theCount(self):
        return(self.theCount)

    def incr_theCount(self):
        self.theCount += 1
        return

    def get_nonTarget(self):
        return(self.nonTarget)

    def add_nonTarget(self, w):
        self.nonTarget.append(w)
        return

    def print_config(self,printSorted=True):
        print("-------- Print Config --------")
        ln = len(self.get_target_words())
        print("TargetWords (%d): " % ln, end='')
        if printSorted:
            print(sorted(self.get_target_words()))
        else:
            print(self.get_target_words())
        return

    def print_run_info(self,printSorted=True):
        print("-------- Print Run Info --------")
        print("All words:%3s. " % self.get_allWords(), end='')
        print(" Target words:%3s" % self.get_theCount())
        print("Non-Target words (%d): " % len(self.get_nonTarget()), end='')
        if printSorted:
            print(sorted(self.get_nonTarget()))
        else:
            print(self.get_nonTarget())
        return

    def print_confusion_matrix(self, targetLabel, doKey=False, tag=""):
        assert (self.TP + self.TP + self.FP + self.TN) > 0
        print(tag+"-------- Confusion Matrix --------")
        print(tag+"%10s | %13s" % ('Predict', 'Label'))
        print(tag+"-----------+----------------------")
        print(tag+"%10s | %10s %10s" % (' ', targetLabel, 'not'))
        if doKey:
            print(tag+"%10s | %10s %10s" % ('', 'TP   ', 'FP   '))
        print(tag+"%10s | %10d %10d" % (targetLabel, self.TP, self.FP))
        if doKey:
            print(tag+"%10s | %10s %10s" % ('', 'FN   ', 'TN   '))
        print(tag+"%10s | %10d %10d" % ('not', self.FN, self.TN))
        return

    def eval_training_set(self, tset, targetLabel, lines=True):
        print("-------- Evaluate Training Set --------")
        self.initTF()
        # zip is good for parallel arrays and iteration
        z = zip(tset.get_instances(), tset.get_lines())
        for ti, w in z:
            lb = ti.get_label()
            cl = ti.get_class()
            if lb == targetLabel:
                if cl:
                    self.TP += 1
                    outcome = "TP"
                else:
                    self.FN += 1
                    outcome = "FN"
            else:
                if cl:
                    self.FP += 1
                    outcome = "FP"
                else:
                    self.TN += 1
                    outcome = "TN"
            explain = ti.get_explain()
            # Format nice output
            if lines:
                w = ' '.join(w.split())
            else:
                w = ' '.join(ti.get_words())
                w = lb + " " + w

            # TW = testing bag of words words (kinda arbitrary)
            print("TW %s: ( %10s) %s" % (outcome, explain, w))
            if Debug:
                print("-->", ti.get_words())
        self.print_confusion_matrix(targetLabel)
        return

    def classify_by_words(self, ti, update=False, tlabel="last"):
        inClass = False
        evidence = ''
        lw = ti.get_words()
        for w in lw:
            if update:
                self.incr_allWords()
            if w in self.get_target_words():    # FIXME Write predicate
                inClass = True
                if update:
                    self.incr_theCount()
                if evidence == '':
                    evidence = w            # FIXME Use first word, but change
            elif w != '':
                if update and (w not in self.get_nonTarget()):
                    self.add_nonTarget(w)
        if evidence == '':
            evidence = '#negative'
        if update:
            ti.set_class(inClass, tlabel, evidence)
        return(inClass, evidence)

    # Could use a decorator, but not now
    def classify(self, ti, update=False, tlabel="last"):
        cl, e = self.classify_by_words(ti, update, tlabel)
        return(cl, e)

    def classify_all(self, ts, update=True, tlabel="classify_all"):
        for ti in ts.get_instances():
            cl, e = self.classify(ti, update=update, tlabel=tlabel)
        return


class ClassifyByTopN(ClassifyByTarget):
    def __init__(self, lw=[]):
        super().__init__(lw=lw)
        self.freq_dict = {}
        self.descend_values = []

    def target_top_n(self, tset, num=5, label=''):
        """ Finds and sets target words to the num most common words in the given TrainingSet. Note that the len of target words
        may exceed num in cases where there are ties between word frequencies.
        
        Arguments:
            tset (TrainingSet): TrainingSet object used to obtain target words
            num (int): Minimum len of target words. len exceeds num if there is a tie between how frequently some n words appear.
            label (str): Label to look for target words in. If label does not match within a TrainingInstance, its words are excluded.
            
        Returns:
            none
        """
        most_common = []
        
        self.set_freq_dict(tset.get_instances(), label)
        self.set_descending_freq()

        count = 0
        freq = 0
        while count < num or self.common_tie(freq):
            word, freq = self.get_top_common()
            most_common.append(word)

            count += 1

        self.set_target_words(most_common)
            
    def get_top_common(self):
        """ Obtains and returns tuple of the word with the current greatest frequency found in self.freq_dict.
        
        Arguments:
            none
            
        Returns:
            (str, int): Tuple of str word and its int frequency
        """
        value = self.descend_values[0]

        for key in self.freq_dict:
            if self.freq_dict[key] == value:
                self.descend_values.pop(0)
                self.freq_dict.pop(key)

                return key, value

    def common_tie(self, last_common):
        """ Checks whether there is a tie in frequency between the previous word and any of the words in self.freq_dict.
        
        Arguments:
            last_common (int): Frequency count of the previous word.
            
        Returns:
            (bool): bool representing whether there is a tie of frequency
        """
        return last_common in self.freq_dict.values()

    def set_descending_freq(self):
        """ Sets self.descend_values to a descending list of all the values within the self.freq_dict dictionary.
        
        Arguments:
            none
            
        Returns:
            none
        """
        self.descend_values = sorted(self.freq_dict.values(), reverse=True)
            
    def set_freq_dict(self, ti_list, label):
        """ Collects all words within the given list of TrainingInstance objects and stores them ina dictionary with key-value
        pairs of [word]: [frequency]. 
        
        Arguments:
            ti_list (list): List of TrainingInstance objects
            label (str): String of TrainingInstance label to look for
            
        Returns:
            none
        """
        self.freq_dict = {}
        for ti in ti_list:
            if ti.get_label() == label:
                inst_words = ti.get_words()

                for word in inst_words:

                        if word not in self.freq_dict:
                            self.freq_dict[word] = 1

                        else:
                            self.freq_dict[word] += 1


class TrainingInstance(C274):
    def __init__(self):
        super().__init__() # Call superclass
        # self.type = str(self.__class__)
        self.inst = dict()
        # FIXME:  Get rid of dict, and use attributes
        self.inst["label"] = "N/A"      # Class, given by oracle
        self.inst["words"] = []         # Bag of words
        self.inst["class"] = ""         # Class, by classifier
        self.inst["explain"] = ""       # Explanation for classification
        self.inst["experiments"] = dict()   # Previous classifier runs
        return

    def get_label(self):
        return(self.inst["label"])

    def get_words(self):
        return(self.inst["words"])

    def set_words(self, wordList):
        """ Sets and overrides the previous word list into the one provided.
        
        Arguments:
            wordList (list): new list of words to set within instance
            
        Returns:
            none
        """
        self.inst["words"] = wordList

    def set_class(self, theClass, tlabel="last", explain=""):
        # tlabel = tag label
        self.inst["class"] = theClass
        self.inst["experiments"][tlabel] = theClass
        self.inst["explain"] = explain
        return

    def get_class_by_tag(self, tlabel):             # tlabel = tag label
        cl = self.inst["experiments"].get(tlabel)
        if cl is None:
            return("N/A")
        else:
            return(cl)

    def get_explain(self):
        cl = self.inst.get("explain")
        if cl is None:
            return("N/A")
        else:
            return(cl)

    def get_class(self):
        return self.inst["class"]

    def process_input_line(
                self, line, run=None,
                tlabel="read", inclLabel=False
            ):
        for w in line.split():
            if w[0] == "#":
                self.inst["label"] = w
                if inclLabel:
                    self.inst["words"].append(w)
            else:
                self.inst["words"].append(w)

        if not (run is None):
            cl, e = run.classify(self, update=True, tlabel=tlabel)
        return(self)

    def preprocess_words(self, mode=''):
        """ Performs preprocessing on list of words contained in self.inst['words']. Preprocessing occurs word-by-word via helper
        method 'preprocess_word(word, mode)'.
        
        Arguments:
            mode (str): string of the specific preprocessing mode to use
            
        Returns:
            none
        """
        words = self.get_words()
        processed_words = []

        # Perform preprocessing on words one by one
        for word in words:
            processed_word = self.preprocess_word(word, mode)
            
            # Add preprocessed word to the list if it is not empty string
            if processed_word:
                processed_words.append(processed_word)

        self.set_words(processed_words)

    def preprocess_word(self, word, mode):
        """ Performs preprocessing on a given word. When no mode is given, all symbols, stopwords, and numeric digits are removed
        (unless the string is only composed of numeric digits). Symbol, stopword, and numeric digits can be turned off one at a time 
        via the mode parameter. Note that the mode parameter must match a string literal exactly (i.e. case sensitive).

        Arguments:
            word (str): string of the word to perform preprocessing on
            mode (str): string of the specific preprocessing mode to use

        Returns:
            word (str): string of the preprocessed word or an empty string if the given word argument is a stopword and keep-stops mode
                        is not selected
        """
        # Turn all chars to lowercase in word if possible
        word = word.lower()

        # Remove symbol chars if keep-symbols mode off
        if mode != "keep-symbols":
            word = self.remove_symbols(word)

        # Return entire token if completely composed of numbers
        if self.is_str_num(word):
            return word

        # Return empty str if keep-symbols mode off and str is stopword
        if mode != "keep-stops" and self.is_stopword(word):
            return ""

        # Remove all numbers from word if keep-digits mode is off
        if mode != "keep-digits":
            return self.remove_nums(word)
        else:
            return word

    def remove_symbols(self, word):
        """ Removes symbolic characters from a given string.

        Arguments:
            word (str): string of the word to remove symbols from

        Returns:
            noSymbolWord (str): new string of the given word without symbols
        """
        noSymbolWord = ""

        for letter in word:
            if letter.isalpha() or letter.isnumeric():
                noSymbolWord += letter

        return noSymbolWord
            
    def is_str_num(self, word):
        """ Returns bool of whether the given string is fully composed of numeric digits.

        Arguments:
            word (str): string of the word to check

        Returns:
            (boolean): bool value of whether the string is only numeric digits"""
        return word.isnumeric()

    def is_stopword(self, word):
        """ Returns bool of whether the given string parameter is a stopword. Note that the parameter must be in lowercase.

        Arguments:
            word (str): lowercase string of the word to check

        Returns:
            (boolean): bool value of whether the word is a stopword
        """
        stopwords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", 
            "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", 
            "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", 
            "themselves", "what", "which","who", "whom", "this", "that", "these", "those", 
            "am", "is", "are", "was", "were", "be","been", "being", "have", "has", "had", 
            "having", "do", "does", "did", "doing", "a", "an","the", "and", "but", "if", 
            "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", 
            "about", "against", "between", "into", "through", "during", "before", "after", 
            "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over",
            "under", "again", "further", "then", "once", "here", "there", "when", "where", 
            "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", 
            "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", 
            "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

        return word in stopwords

    def remove_nums(self, word):
        """ Removes all numeric digits from the given string.

        Arguments:
            word (str): string of the word to remove numeric digits from

        Returns:
            noNumWord (str): new string of the original word without numeric digits
        """
        noNumWord = ""
        for letter in word:
            if not letter.isnumeric():
                noNumWord += letter

        return noNumWord


class TrainingSet(C274):
    def __init__(self):
        super().__init__() # Call superclass
        # self.type = str(self.__class__)
        self.inObjList = []     # Unparsed lines, from training set
        self.inObjHash = []     # Parsed lines, in dictionary/hash
        self.variable = dict()  # NEW: Configuration/environment variables
        return

    def set_env_variable(self, k, v):
        self.variable[k] = v
        return

    def get_env_variable(self, k):
        if k in self.variable:
            return(self.variable[k])
        else:
            return ""

    def inspect_comment(self, line):
        if len(line) > 1 and line[1] != ' ':      # Might be variable
            v = line.split(maxsplit=1)
            self.set_env_variable(v[0][1:], v[1])
        return

    def get_instances(self):
        return(self.inObjHash)      # FIXME Should protect this more

    def get_lines(self):
        return(self.inObjList)      # FIXME Should protect this more

    def print_training_set(self):
        print("-------- Print Training Set --------")
        z = zip(self.inObjHash, self.inObjList)
        for ti, w in z:
            lb = ti.get_label()
            cl = ti.get_class_by_tag("last")     # Not used
            explain = ti.get_explain()
            print("( %s) (%s) %s" % (lb, explain, w))
            if Debug:
                print("-->", ti.get_words())
        return

    def process_input_stream(self, inFile, run=None):
        assert not (inFile is None), "Assume valid file object"
        cFlag = True
        while cFlag:
            line, cFlag = safe_input(inFile)
            if not cFlag:
                break
            assert cFlag, "Assume valid input hereafter"

            if len(line) == 0:   # Blank line.  Skip it.
                continue

            # Check for comments *and* environment variables
            if line[0] == '%':  # Comments must start with % and variables
                self.inspect_comment(line)
                continue

            # Save the training data input, by line
            self.inObjList.append(line)
            # Save the training data input, after parsing
            ti = TrainingInstance()
            ti.process_input_line(line, run=run)
            self.inObjHash.append(ti)
        return

    def preprocess(self, mode=''):
        """ Calls training instances within self to perform preprocessing on each of their respective list of words.

        Arguments:
            mode (str): string of the specific preprocessing mode to use
            
        Returns:
            none

        """
        instances = self.get_instances()

        for instance in instances:
            instance.preprocess_words(mode)

    def copy(self):
        """ Returns a deepcopy of the object from which copy is invoked from.
        
        Arguments:
            none
            
        Returns:
            ts_copy (TrainingSet): deepcopy of self
        """
        ts_copy = copy.deepcopy(self)
        return ts_copy

    def add_training_set(self, tset):
        """ Creates deepcopy of given TrainingSet object's lines and TrainingInstance objects and appends 
        to self's respective list attribute.
        
        Arguments:
            tset (TrainingSet): TrainingInstance object to add instances and lines from
            
        Returns:
            none
        """
        ti_list = copy.deepcopy(tset.get_instances())
        line_list = copy.deepcopy(tset.get_lines())
        self.inObjHash += ti_list
        self.inObjList += line_list

    def return_nfolds(self, num=3):
        """ Performs round robin folding via creating num copies of self and allocating a different section of TrainingInstance
        objects to each respective copy.
        
        Arguments:
            num (int): Number of folds 
            
        Returns:
            folded_ts_list (list): List containing num TrainingSet objects with respective folds
        """
        folded_ts_list = []
        ti_list = self.get_instances()
        lines_list = self.get_lines()
        ti_len = len(ti_list)
        
        fold_indices = self.return_fold_indices(ti_len, num)
        

        for sub_fold in fold_indices:
            # Allocate respective folds for each copy
            ts_fold = self.copy()

            # Clear TrainingSet copy instance and line attrs
            ts_fold.set_instances([])
            ts_fold.set_lines([])

            for fold in sub_fold:
                # Add TrainingInstance objects one by one to copy
                ts_fold.add_instance(ti_list[fold])
                ts_fold.add_line(lines_list[fold])

            folded_ts_list.append(ts_fold)
                
        return folded_ts_list

    def return_fold_indices(self, ti_len, num):
        """ Allocates a number of indices within the list of TrainingInstance objects to each fold. Indices are picked using a round robin
        strategy. If ti_len does not fold evenly into num, then some sublists in fold_indices will contain one more or less indices. 
        
        Arguments:
            ti_len (int): len of the list of TrainingInstance objects
            num (int): Number of folds 
            
        Returns:
            fold_indices (list): list containing num sublists which respectively contain the indicies of the TrainingInstance objects to select
        """
        fold_indices = [[] for i in range(num)]
        increment = ti_len // num 

        if ti_len % num != 0:
            increment += 1

        i = 0
        for j in range(ti_len):
            fold_indices[i].append(j)

            i = (i + 1) % num

        return fold_indices

    def add_instance(self, ti):
        """ Adds the given TrainingInstance object to self's list of instances.
        
        Arguments:
            ti (TrainingInstance): TrainingInstance object to append 
            
        Returns:
            none
        """
        self.inObjHash.append(ti)

    def add_line(self, line):
        """ Adds the given line to self's list of lines.
        
        Arguments:
            line (str): str of the line to append to self
            
        Returns:
            none
        """
        self.inObjList.append(line)

    def set_instances(self, ti_list):
        """ Sets the given list of TrainingInstance object(s) to self
        
        Arguments:
            ti_list (list): New list of TrainingInstance objects to set
            
        Returns:
            none
        """
        self.inObjHash = ti_list

    def set_lines(self, line_list):
        """ Sets the given list of lines to self
        
        Arguments:
            line_list (list): New list of lines to set
            
        Returns:
            none
        """
        self.inObjList = line_list


# Very basic test of functionality
def basemain():
    global Debug
    tset = TrainingSet()
    run1 = ClassifyByTarget(TargetWords)
    if Debug:
        print(run1)     # Just to show __str__
        lr = [run1]
        print(lr)       # Just to show __repr__

    argc = len(sys.argv)
    if argc == 1:   # Use stdin, or default filename
        inFile = open_file()
        assert not (inFile is None), "Assume valid file object"
        tset.process_input_stream(inFile, run1)
        inFile.close()
    else:
        for f in sys.argv[1:]:
            # Allow override of Debug from command line
            if f == "Debug":
                Debug = True
                continue
            if f == "NoDebug":
                Debug = False
                continue

            inFile = open_file(f)
            assert not (inFile is None), "Assume valid file object"
            tset.process_input_stream(inFile, run1)
            inFile.close()

    print("--------------------------------------------")
    plabel = tset.get_env_variable("pos-label")
    print("pos-label: ", plabel)
    print("NOTE: Not using any target words from the file itself")
    print("--------------------------------------------")

    if Debug:
        tset.print_training_set()
    run1.print_config()
    run1.print_run_info()
    run1.eval_training_set(tset, plabel)

    return


if __name__ == "__main__":
    basemain()