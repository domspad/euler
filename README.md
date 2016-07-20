
## Project Euler

These are my solutions to [project euler](https://projecteuler.net/) problems in Python. My main goal was to obtain the solution as fast as possible, whatever means necessary (i.e. get the solution first, then worry about code structure and layout). I would record the times from when I started the problem, to when I had the solution. These are listed in `time.csv`. I would also record the runtime of the code.

I'm now working on refactoring the solutions and factoring out common functions and code to identify the underlying functions I used in many solutions. 

##Analyse data!

```
import pandas as pd

df = pd.read_table('time.csv',sep=',')

# wall time grows with brute number
df[df.brute_number.notnull()].plot('brute_number','wall_time',kind='scatter',logx=True,logy=True)

# difficulty vs solve time
sdf = df.groupby('difficulty').median()
sdf['difficulty'] = sdf.index.tolist()
sdf.plot('difficulty','to_complete',kind='scatter')

# problem_num vs solve time
df.plot('num','to_complete',kind='scatter')
df.plot('num','difficulty',kind='scatter')

# hours spent solving and waiting for run to finish
df.to_complete.sum()/60
```

To profile programs:

	`python -m cProfile <script>`

To RunSnakeRun bottleneck analyze

	`python -m cProfile -o <script_name.out> <script>`
	`sudo python /Users/dominicspadacene/Library/Enthought/Canopy_64bit/User/lib/python2.7/site-packages/runsnakerun/runsnake.py <script_name.out>`

	<!-- yes this is ugly :( -->