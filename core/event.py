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

    def remove(self, subscriber: Callable[[T], Any]):
        self._subscribers.remove(subscriber)


if __name__ == "__main__":
    event: Event[str] = Event()
    event2: Event[int] = Event()


    class AA:
        def event_listener(self, x: str):
            print(x)

        def event_listener2(self, x: int):
            print(x)

        def event_listener3(self, x: str):
            print(x * 5)

    b = AA()
    a = AA()
    # event.add(a.event_listener2) pokazuje error bo bad signature
    event.add(b.event_listener3)
    event2.add(a.event_listener2)

    event.invoke("aaa")
    event.invoke("AAA")
    event.invoke("bbb")

    event2.invoke(123131)
