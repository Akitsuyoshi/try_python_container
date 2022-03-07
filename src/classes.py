from typing import Any, Optional, Sequence


class Vector:
    """Create d-dimentional vector of zeroes
    """

    def __init__(self, d: int) -> None:
        self._coords = [0] * d

    def __len__(self) -> int:
        return len(self._coords)

    def __getitem__(self, j) -> int:
        return self._coords[j]

    def __setitem__(self, j, val) -> None:
        self._coords[j] = val

    def __add__(self, other: 'Vector') -> 'Vector':
        if len(self) != len(other):
            raise ValueError('dimensions must agree')

        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other: 'Vector') -> bool:
        return self._coords == other._coords

    def __ne__(self, other: 'Vector') -> bool:
        return not self == other  # rely on exsisting __eq__ definition

    def __str__(self) -> str:
        return '<' + str(self._coords)[1: -1] + '>'


class SequenceIterator:
    """An iterator for any of Python's sequence types
    """
    def __init__(self, sequence: Sequence) -> None:
        self._seq = sequence
        self._k = -1  # will increment to 0 on first call to next

    def _next_(self) -> Any:
        self._k += 1
        if self._k < len(self._seq):
            return (self._seq[self._k])
        else:
            raise StopIteration()

    def __iter__(self):
        """By convenction, an iterator must return itself as an iterator
        """
        return self


class Range:
    """A class that mimic's built-in range class
    """
    def __init__(self, start: int, stop: Optional[int] = None, step: int = 1) -> None:
        if step == 0:
            raise ValueError('step cannot be 0')
        if stop is None:
            start, stop = 0, start  # should be treated as if range(0, n)

        # calculate the effective length once
        self._length = max(0, (stop - start + step - 1) // step)

        # need knowledge of start and step(but not stop) to support __getitem__
        self._start = start
        self._step = step

    def __len__(self) -> int:
        return self._length

    def __getitem__(self, k: int) -> int:
        if k < 0:
            k += len(self)  # attempt to convert negative index
        if not 0 <= k < self._length:
            raise IndexError('Index out of range')

        return self._start + k * self._step


class Progression:
    """Iterator producing a generic progression.
    Default iterator produces the whole numbers, 0, 1, 2 ..
    """
    def __init__(self, start: int = 0) -> None:
        self._current = start

    def _advance(self) -> None:
        self._current += 1

    def __next__(self) -> int:
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self) -> 'Progression':
        return self

    def print_progression(self, n: int) -> None:
        print(' '.join(str(next(self)) for _ in range(n)))


class ArithmaticProgression(Progression):
    """Iterator producint an arithmatic progressin

    Args:
        Progression (_type_):
    """
    def __init__(self, increment: int = 1, start: int = 0) -> None:
        super().__init__(start)
        self._increment = increment

    def _advance(self) -> None:
        self._current += self._increment


class GeomatricProgression(Progression):
    """Iterator producing a new geomatirc progression.

    Args:
        Progression (_type_):
    """
    def __init__(self, base: int = 2, start: int = 1) -> None:
        super().__init__(start)
        self._base = base

    def _advance(self) -> None:
        self._current *= self._base


class FibonacciProgression(Progression):
    """Iterator producing a generalized Fibonacci progression

    Args:
        Progression (_type_):
    """
    def __init__(self, first: int = 0, second: int = 1) -> None:
        super().__init__(first)
        self._prev = second - first

    def _advance(self) -> None:
        self._prev, self._current = self._current, self._prev + self._current


if __name__ == '__main__':
    v = Vector(5)
    v[1] = 23
    v[-1] = 45
    print(v[4])
    u = v + v
    print(u)
    total = 0
    for entry in v:
        total += entry
    print(total)
    print(str(v))

    print(' Default progression: ')
    Progression().print_progression(10)
    print('Arithmetic progression with increment 5:')
    ArithmaticProgression(5).print_progression(10)
    print('Arithmetic progression with increment 5 and start 2:')
    ArithmaticProgression(5, 2).print_progression(10)
    print('Geometric progression with default base:')
    GeomatricProgression().print_progression(10)
    print('Geometric progression with base 3:')
    GeomatricProgression(3).print_progression(10)
    print('Fibonacci progression with default start values:')
    FibonacciProgression().print_progression(10)
    print('Fibonacci progression with start values 4 and 6:')
    FibonacciProgression(4, 6).print_progression(10)
