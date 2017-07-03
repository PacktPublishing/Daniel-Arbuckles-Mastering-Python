"""A zoo 'simulation'

Demonstrates the Observer and Observable classes from reactive.py

"""

import asyncio
import random

from .reactive import Observer, Observable


class AnimalEvent:
    def __init__(self, source, action, value = ''):
        self.source = source
        self.action = action
        self.value = value


class Animal(Observable):
    def __init__(self, name, sound):
        super().__init__()
        self.name = name
        self.sound = sound

    async def run(self):
        while True:
            await asyncio.sleep(random.random() * 10)

            if random.random() < 0.01:
                self._event(AnimalEvent(self, 'die'))
                self._complete()
                return

            self._event(AnimalEvent(self, 'noise', self.sound))


class SometimesLoud(Observable, Observer):
    def __init__(self, *sources):
        super().__init__()

        self.sources = sources

        for source in sources:
            source.subscribe(self)

    def on_event(self, event):
        if event.action == 'noise' and random.random() < 0.25:
            self._event(AnimalEvent(event.source,
                                    event.action,
                                    '{} loudly'.format(event.value)))
        else:
            self._event(event)

    def on_complete(self):
        if all(x.complete for x in self.sources):
            self._complete()


class Output(Observer):
    def __init__(self, *sources):
        super().__init__()
        for source in sources:
            source.subscribe(self)

    def on_event(self, event):
        if event.action == 'die':
            print(event.source.name, 'died!')
        else:
            print(event.source.name, event.value)


def zoo():
    elephant = Animal('Lucretia', 'trumpets')
    lion = Animal('Arnold', 'roars')
    fox = Animal('Betty', 'goes chacha-chacha-chacha-chow')
    snake = Animal('Jake', 'hisses')

    out = Output(fox, snake, SometimesLoud(elephant, lion))

    return asyncio.gather(elephant.run(), lion.run(), fox.run(), snake.run())
