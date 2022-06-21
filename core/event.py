from __future__ import annotations

from typing import Generic, TypeVar, Callable, Any, Optional, List

T = TypeVar('T')


class Event(Generic[T]):

    _subscribers: List[Callable[[T], Any]]

    def __init__(self):
        self._subscribers = []

    def invoke(self, data: T):
        for subscriber in self._subscribers:
            subscriber(data)

    def add(self, subscriber: Callable[[T], Any]):
        self._subscribers.append(subscriber)


if __name__ == "__main__":
    event: Event[str] = Event()
    event2: Event[int] = Event()

    def event_listener(x: str):
        print(x)

    def event_listener2(x: int):
        print(x)

    def event_listener3(x: str):
        print(x * 5)

    event.add(event_listener)
    # event.add(event_listener2) pokazuje error bo bad signature
    event.add(event_listener3)
    event2.add(event_listener2)

    event.invoke("aaa")
    event.invoke("AAA")

    event2.invoke(123131)
