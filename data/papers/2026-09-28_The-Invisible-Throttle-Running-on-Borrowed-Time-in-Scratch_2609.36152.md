# The Invisible Throttle: Running on Borrowed Time in Scratch

- arXiv ID: `2609.36152v1`
- Authors: Xinyue Feng, Hanyuan Shi, Yuan Si
- Published: 2026-09-28
- Primary category: `cs.SE`
- Categories: `cs.SE`
- Links: [abs](http://arxiv.org/abs/2609.36152v1) | [pdf](https://arxiv.org/pdf/2609.36152v1)

## Abstract

Scratch has 135 million registered users, most of them children, and 164 million shared projects. What they are taught about the speed of a script fits in one sentence: a loop iterates once per frame. Unfortunately, that sentence describes the exception. In the public virtual machine a frame repeats the scripts until something visible asks the screen to redraw, no script is left running, or three quarters of the frame's wall-clock time are spent. Hence a loop that does not draw is paced by whatever else is visible and by the machine. Hide the moving sprite of a two-sprite project, and the other's counting loop runs 77,000 times faster on a laptop. No documentation states the rule. Our key observation is that the redraw gate is one flag for the whole runtime, so a loop's speed can be changed without touching its code: hide the sprite that draws, change the machine's budget, or run the program in a tool with no renderer. ThrottleCheck implements a budgeted semantics (a stated budget of rounds per frame, the redraw gate emulated) on the unmodified virtual machine, runs a project under each knob, and reports a rate-sensitive project with a witness. On 500 popular public games, 59% contain a loop that never draws and never waits. Muting the requests of the sprites that draw changes the state of a played game after ten seconds in 24% of the games that have one; hiding them changes 18%; running the game without a renderer and without the gate changes 61%. Rules that read a position, a score or a clock after a fixed time reverse between pass and fail once the throttle is released, in 17% of Whisker's own example tests and 19% of a tutorial's checks on 224 of its remixes. A grader without a renderer grades a program the editor never runs, unless it emulates the gate and states a budget; we say what graders and the platform should do, and close with the sentence a child could be taught.
