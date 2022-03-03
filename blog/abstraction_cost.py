from typing_extensions import Required


Abstraction cost
26/11/2021, 14:23:21
programming, performance optimization
What is abstraction cost? When does it matter?
Generally speaking abstraction cost refers to any performance hits incurred when using or creating abstractions (programming languages, coding artefacts, etc) which makes it slower for a machine to execute. Interestingly enough either this is one of the most critical aspects of a piece of software (eg: network components, database applications, numerical method solvers, high frequency trading systems, etc.) or it is hardly relevant to the problem at all. In the latter situation the engineering cost outweight by many order of magnitude any benefit that could be gained by optimizing performances. To labour the point non critical performance optimization can be compared to using precious metals in plumbing. It will not make any difference to the end users but for the engineering cost. Now that is not to say that you should never be mindful of performances and write code in completely naive way. On the contrary one should always have at least a rough idea of the intrinsic overall computational effort required to perform. In many situations this effort is small enough that one can choose to use "slow" technologies or even write "slow" code (unknowingly or not) without making any difference in terms of perceived value. In more complex situations a proper appreciation 
of not making design decision which will harm performances.  
Put it another way I would go as far as saying that if performance are not critical it means that we should 


a given task to have a rough idea of the theoritical minimum. In  and come up with a solution that will perform decently from an end users point of view.

Rather realizing the problem computational requirements and shamelessly leveraging on well optimized data structures and algorithms will yield the best bang for your buck. 
I cannot recommand enough using a code profiler from time to to time just to remind yourself that  