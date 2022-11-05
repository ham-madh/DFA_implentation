class checking_DFA:
    initial_state = 0
    word = ''
    valid = False
    current_state = 0

    def int(self):
        self.word = ''
        self.initial_state = 0
        self.valid = False

    def constructor(self, w, i):
        self.word = w
        self.initial_state = i

    def transition(self, alphabet, state):
        if state == 0:
            if alphabet == 0:
                state = 1
            elif alphabet == 1:
                state = 3
            else:
                print("Invalid Character: ", alphabet)
        elif state == 1:
            if alphabet == 0:
                state = 0
            elif alphabet == 1:
                state = 2
            else:
                print("Invalid Character: ", alphabet)
        elif state == 2:
            if alphabet == 0:
                state = 3
            elif alphabet == 1:
                state = 1
            else:
                print("Invalid Character: ", alphabet)
        elif state == 3:
            if alphabet == 0:
                state = 2
            elif alphabet == 1:
                state = 0
            else:
                print("Invalid Character: ", alphabet)
        return state

    def DFA_working(self, new_word):
        self.word = new_word
        for i in self.word:
            self.current_state = self.transition(int(i), self.current_state)
        if self.current_state == 0:
            print("String is valid.")
        else:
            print("String is invalid.")
if __name__== "__main__":
    string_1 = str(input("Enter the String to check whether its valid or invalid : "))
    S = checking_DFA()
    S.DFA_working(string_1)