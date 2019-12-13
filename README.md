# FSM

## State Transition for AWAKE
AWAKE -SLEEPING-> SLEEP

AWAKE -EATING-> EAT

AWAKE -COOING->IDEL

AWAKE -USING_FORCE-> FORCE

## State Transition for SLEEP
SLEEP - WOKEN UP-> AWAKE

## State Transition for EAT
EAT -SLEEPING-> SLEEP

EAT -COOING-> IDEL

EAT -USING_FORCE-> FORCE


## State Transition for IDEL
IDEL -SLEEPING-> SLEEP

IDEL -COOING-> EAT

IDEL -USING_FORCE-> FORCE

## State Transition for FORCE
FORCE -SLEEPING-> SLEEP

FORCE -COOING-> EAT




