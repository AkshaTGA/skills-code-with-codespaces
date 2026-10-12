#!/usr/bin/env python3
"""Search for large Mersenne primes: numbers of the form 2**p - 1."""

import argparse


def is_prime(number: int) -> bool:
	"""Return whether a positive integer is prime."""
	if number < 2:
		return False
	if number % 2 == 0:
		return number == 2
	divisor = 3
	while divisor * divisor <= number:
		if number % divisor == 0:
			return False
		divisor += 2
	return True


def is_mersenne_prime(exponent: int) -> bool:
	"""Return whether 2**exponent - 1 is prime using Lucas-Lehmer."""
	if exponent == 2:
		return True
	if exponent < 2 or not is_prime(exponent):
		return False

	mersenne = (1 << exponent) - 1
	value = 4
	for _ in range(exponent - 2):
		value = (value * value - 2) % mersenne
	return value == 0


def main() -> None:
	parser = argparse.ArgumentParser(
		description="Find Mersenne primes 2**p - 1."
	)
	parser.add_argument(
		"--start",
		type=int,
		default=2,
		help="First exponent to test (default: 2).",
	)
	parser.add_argument(
		"--count",
		type=int,
		default=1,
		help="Number of Mersenne primes to find (default: 1).",
	)
	args = parser.parse_args()

	if args.start < 2 or args.count < 1:
		parser.error("--start must be at least 2 and --count must be positive")

	found = 0
	exponent = args.start
	while found < args.count:
		print(f"Testing p={exponent}...", flush=True)
		if is_mersenne_prime(exponent):
			number = (1 << exponent) - 1
			print(f"\nMersenne prime found! p={exponent}")
			print(f"Digits: {len(str(number))}")
			print(number)
			found += 1
		exponent += 1


if __name__ == "__main__":
	main()
