---
layout: post
title: "[Competitive Programming] Pokemons"
date: 2018-11-10
---

# The problem

Located here: [http://primers.xyz/3](http://primers.xyz/3). The website is in french, here is a quick translation :

> Welcome to Primers, a site dedicated to algorithmic problems whose optimal solution is not achievable in a reasonable time. We must therefore design algorithms to find approximate solutions. Your goal: to do better than your competitors! :)

>PROBLEM: In the first generation of Pokemon, there are 164 different attacks. Each Pokemon can learn a number of attacks. As a Pokemon trainer, you want to be the team of 6 Pokemon whose union of attacks they can learn is maximum.

So it is a bit like the old Google Code Jam: you execute your code locally and give back to the website your best solution, then the website gives you a ranking.

Regarding the Pokemon problem, my first approach was to do random hill climbing: start with an initial solution (=a team of 6 pokemon), and randomly replace one of the Pokemon with an other random one. If this yield a better score, continue to iterate with this new team. With a small Python script, I achieved a score of 104.

Returning on the website, I could see in the ranking table that the best score was 105. Some comments were hinting that an optimal solution could be found for this problem.

For sure, an optimal solution would be to enumerate all the teams that can be created with 6 Pokemons. This is called brute-forcing the problem, could it be done here ?

How many [combinations](https://en.wikipedia.org/wiki/Combination) of 6 pokemons out of 150 are they ? 

If the set has n elements, the number of k-combinations is equal to the binomial coefficient : 

$$\binom{n}{k} = \frac{n(n-1)...(n-k+1)}{k(k-1)...1}$$

```sh
>>> import scipy.misc
>>> scipy.misc.comb(150, 6, exact=True)
14297000725
```

So there is about 14 billions of combinations to test.If you can test 1 billion of combinations per seconds, it will take 14 seconds... Today processors are running north of 1 GHz, so it is something reachable.

To achieve that performance, Python was not possible, therefore I wrote a solution in C. Of course you better turn the optimisation on when doing that (-O3 for example).

Some colleague of mine was doubtful that it was possible to test a combination on a single CPU cycle.

Of course, you need more, but if coded well the inner loop (that test one combination) can take in the order of 10 instructions.

If only they had put a more difficult problem, for example teams of 8+ pokemons or a set of 250 different pokemons, then it would have been almost impossible to brute-force the problem ...
​
# The solution

See [pokemon.c](https://github.com/jeyries/pokemon/blob/master/pokemon.c) in my Github repository.

Below is the assembly produced with `gcc-8 -O3 -march=native`. GCC does a very good job here, the inner loop is straightforward : 3 OR + 3 POPCNT per test, a good x86-64 processor will be crushing through all the combinations in a few seconds ...

```asm
L7:
	movq	(%rdx), %rax
	movq	8(%rdx), %rsi
	movq	16(%rdx), %rcx
	orq	%r10, %rax
	orq	%r9, %rsi
	popcnt	%rax, %rax
	popcnt	%rsi, %rsi
	orq	%r8, %rcx
	addl	%esi, %eax
	popcnt	%rcx, %rcx
	addl	%ecx, %eax
	cmpl	%ebp, %eax
	jle	L6
	movb	7(%rsp), %cl
	movb	6(%rsp), %sil
	movb	$1, 4(%rsp)
	movl	%eax, %ebp
	movb	5(%rsp), %r15b
	movb	1(%rsp), %r13b
	movb	%bl, %r14b
	movb	%dil, %r12b
	movb	%cl, 3(%rsp)
	movb	%sil, 2(%rsp)
L6:
	incl	%edi
	addq	$24, %rdx
	cmpl	%r11d, %edi
	jne	L7
```

