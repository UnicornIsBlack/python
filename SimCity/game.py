from simcity import SimCity


class Game:
    sim = SimCity()
    cmd = [
        'help',
        'demand',
        'search',
        'quit'
    ]

    def __init__(self):
        self.start()

    def start(self):
        while True:
            command = input('=>').lower()
            if command == 'help':
                print(self.cmd)
            elif command == 'demand':
                self.sim.complete_input()
            elif command == 'search':
                self.sim.print_demand()
            elif command == 'quit':
                break
            else:
                pass


game = Game()
