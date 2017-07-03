"""A zoo 'simulation'

Demonstrates ReactiveX event sequences

"""

import asyncio
import random

import rx


class AnimalEvent:
    def __init__(self, source, action, value = ''):
        self.source = source
        self.action = action
        self.value = value


class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
        self.alive = True

    def generate_event(self):
        if random.random() < 0.01:
            self.alive = False
            return AnimalEvent(self, 'die')
        return AnimalEvent(self, 'noise', self.sound)

    def as_observable(self, scheduler):
        return rx.Observable.generate_with_relative_time(
            self,                              # initial state
            (lambda x: self.alive),            # continue condition
            (lambda x: self),                  # next state
            (lambda x: self.generate_event()), # get next value
            (lambda x: random.random() * 10),  # how long before next cycle
            scheduler
        )


def sometimes_loud(event):
    if event.action == 'noise' and random.random() < 0.25:
        return AnimalEvent(event.source,
                           event.action,
                           '{} loudly'.format(event.value))
    return event


def output(event):
    if event.action == 'die':
        print(event.source.name, 'died!')
    else:
        print(event.source.name, event.value)


def zoo():
    scheduler = rx.concurrency.AsyncIOScheduler()

    elephant = Animal('Lucretia', 'trumpets').as_observable(scheduler)
    lion = Animal('Arnold', 'roars').as_observable(scheduler)
    fox = Animal('Betty', 'goes chacha-chacha-chacha-chow').as_observable(scheduler)
    snake = Animal('Jake', 'hisses').as_observable(scheduler)

    louder = rx.Observable.merge(elephant, lion).select(sometimes_loud)

    out = rx.Observable.merge(fox, snake, louder).do_action(on_next = output)

    done = asyncio.Future()

    out.subscribe(on_completed = (lambda: done.set_result(True)))

    return done
