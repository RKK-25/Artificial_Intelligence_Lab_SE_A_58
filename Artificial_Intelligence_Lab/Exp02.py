from experta import *
class StudentFacts(Fact):
    pass
class CareerExpertSystem(KnowledgeEngine):
    @Rule(StudentFacts(likes='Maths'), StudentFacts(likes='Physics'))
    def mechanical(self):
        print("Suggested Career Path: Mechanical Engineering")
    @Rule(StudentFacts(likes='Programming'), StudentFacts(likes='Maths'))
    def computer(self):
        print("Suggested Career Path: Computer Engineering")
    @Rule(StudentFacts(likes='Biology'), StudentFacts(likes='Chemistry'))
    def biotech(self):
        print("Suggested Career Path: Biotechnology")
    @Rule(StudentFacts(likes='Circuits'), StudentFacts(likes='Maths'))
    def electronics(self):
        print("Suggested Career Path: Electronics Engineering")
    @Rule(StudentFacts(likes='Maths'), StudentFacts(likes='Chemistry'))
    def chemoinfo(self):
        print("Suggested Career Path: Chemoinformatics")
    @Rule(StudentFacts(likes='Biology'), StudentFacts(likes='Maths'))
    def bioinfo(self):
        print("Suggested Career Path: Bioinformatics")
    @Rule(StudentFacts(likes='Physics'), StudentFacts(likes='Chemistry'))
    def nanotech(self):
        print("Suggested Career Path: Nanotechnology")
    @Rule(StudentFacts(likes='Physics'), StudentFacts(likes='Biology'))
    def biophy(self):
        print("Suggested Career Path: Biophysics")
    @Rule(StudentFacts(likes='Programming'), StudentFacts(likes='Physics'))
    def quantum(self) :
        print("Suggested Career Path: Quantum computing")
    @Rule(StudentFacts(likes='Physics'), StudentFacts(likes='Circuits'))
    def semiconductor(self):
        print("Suggested Career Path: Semiconductor Engineering")
    @Rule(StudentFacts(likes='Biology'), StudentFacts(likes='Circuits'))
    def neural(self):
        print("Suggested Career Path: Neural Engineering")

def main():
    engine = CareerExpertSystem()
    engine.reset()
    
    print("Welcome to the Career Path Expert System!")
    print("Available options: Maths , Physics , Chemistry , Circuits , Programming , Biology")
    
    interests = input("Enter your interests separated by commas (e.g., Maths, Physics, Programming): ").split(',')
    for interest in interests:
        engine.declare(StudentFacts(likes=interest.strip()))
    engine.run()
    
if __name__ == "__main__":
    main()

