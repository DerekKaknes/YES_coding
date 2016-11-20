from cmd import Cmd
import string, re

class InvalidCharacter(Exception):
    pass

class Hangman(Cmd, object):
    prompt = '>>> '
    def __init__(self):
        super(Hangman, self).__init__()
        self.answer = None
        self.guesses = []
        self.guesses_remaining = 5
        self.hidden_answer = None

    def do_EOF(self, line):
        print "\nQuitting Hangman..."
        return True

    def do_quit(self, line=''):
        return self.do_EOF(line)

    def has_invalid_chars(self, ch):
        if ch in string.punctuation:
            print "'{}' is not a valid character, punctuation marks not allowed".format(ch)
            return True
        elif ch in '0123456789':
            print "'{}' is not a valid character, numbers not allowed".format(ch)
            return True
        else:
            return False


    def generate_hidden_phrase(self):
        return 'Test phrase'

    def get_new_answer(self):
        while True:
            print "Enter new hidden word or phrase, or hit enter to have me generate one for you:"
            ans = raw_input('>.> ')
            if ans == '':
                self.answer = self.generate_hidden_phrase()
            elif self.has_invalid_chars(ans):
                continue
            else:
                self.answer = ans
            self.hidden_answer = list(re.sub('[a-zA-Z]', '_', self.answer))
            break

    def preloop(self):
        print "*"*10 + " Welcome to YES Hangman!" + "*"*10 + '\n'
        if self.answer is None:
            self.get_new_answer()

    def onecmd(self, line):
        if len(line) !=1:
            print "Guesses cannot be longer than a single letter."
        elif self.has_invalid_chars(line):
            pass
        else:
            self.process_guess(line)

    def process_guess(self, ch):
        if ch in self.guesses:
            print "You have already guessed '{}'".format(ch)
        else:
            self.guesses.append(ch)
            if ch in self.answer:
                print "Good guess!"
                for i, ltr in enumerate(self.answer):
                    if ltr == ch:
                        self.hidden_answer[i] = ch
            else:
                print "Sorry, '{}' is not in the answer".format(ch)
                self.guesses_remaining -=1


    def postcmd(self, stop, line):
        if self.guesses_remaining == 0:
            print "Sorry, Game Over!"
            print "The answer was:"
            print self.answer
            return self.do_quit()
        elif '_' not in self.hidden_answer:
            print "Congrats, you win!"
            return self.do_quit()

    def cmdloop(self):
        self.preloop()
        stop = None
        while not stop:
            print "You have guessed: " + ','.join(self.guesses)
            print ''.join(self.hidden_answer)
            print "You currently have {} incorrect guesses remaining".format(self.guesses_remaining)
            self.stdout.write(self.prompt)
            self.stdout.flush()
            line = self.stdin.readline()
            if not len(line):
                line = 'EOF'
            else:
                line = line.rstrip('\r\n')
            line = self.precmd(line)
            stop = self.onecmd(line)
            stop = self.postcmd(stop, line)
        self.postloop()

if __name__ == '__main__':
    hangman = Hangman()
    hangman.cmdloop()
