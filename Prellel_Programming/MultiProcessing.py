import multiprocessing
import os
import time

def DisplayEven(No):
    print("The parent process ID of DisplayEven method is: ",os.getppid())
    print("The process ID of DisplayEven method is: ",os.getpid())
    for i in range(No):
        if i % 2 == 0:
            print("Even numbers are: ",i)

def DisplayOdd(No):
    print("The parent process ID of DisplayOdd method is: ", os.getppid())
    print("The process ID of DisplayOdd method is: ", os.getpid())
    for i in range(No):
        if i % 2 != 0:
            print("Odd numbers are: ",i)

def main():
    Number = 200
    print("-------------------------------------------------------------------")
    print("The parent ID of main process is: ",os.getppid())
    print("The process ID of main is: ",os.getpid())
    print("-------------------------------------------------------------------")

    P1 = multiprocessing.Process(target=DisplayEven,args=(Number,))
    P2 = multiprocessing.Process(target=DisplayOdd,args=(Number,))

    P1.start()
    P2.start()

    P1.join()
    P2.join()
    
    """
    The below syantax act like parellel processing because both P1 and P2 process
    are ready to executes and we join both process simultaneously.

    P1.start()
    P2.start()
    P1.join() 
    P2.join() 

    P1.run()
    P2.run()
    """
    """
    if we write below syntax then process P1 is get start running, after COMPLETE execution of P1 process P2 
    process gets start. This parellel program runs like serial programming.

    P1.start() # P1 process is ready.
    P1.join() # P1 is join first.
    P2.start() # P2 process is ready.
    P2.join() # P2 is join second.
    """
    print("Hello")
if __name__ == "__main__":
    Start = time.process_time()
    main()
    End = time.process_time()
    print("Total execution time is: ",End - Start)

"""
OUTPUT
-------------------------------------------------------------------
The parent ID of main process is:  16084    # This ID is belongs to command prompt.
The process ID of main is:  18220   # This id is of main method, and this is method from which we call other two method.
-------------------------------------------------------------------
The parent process ID of DisplayEven method is:  18220  # this method is called from main method.
The process ID of DisplayEven method is:  7412  # This id is belongs to DisplayEven method
The parent process ID of DisplayOdd method is:  18220   # this method is called from main method.
The process ID of DisplayOdd method is:  11352  # This ID is belongs to DisplayOdd method.
Even numbers are:  0
Even numbers are:  2
Even numbers are:  4
Even numbers are:  6
Even numbers are:  8
Odd numbers are:  1
Even numbers are:  10
Even numbers are:  12
Even numbers are:  14
Even numbers are:  16
Even numbers are:  18
Odd numbers are:  3
Even numbers are:  20
Odd numbers are:  5
Even numbers are:  22
Odd numbers are:  7
Even numbers are:  24
Even numbers are:  26
Even numbers are:  28
Odd numbers are:  9
Odd numbers are:  11
Odd numbers are:  13
Even numbers are:  30
Even numbers are:  32
Even numbers are:  34
Even numbers are:  36
Even numbers are:  38
Even numbers are:  40
Even numbers are:  42
Even numbers are:  44
Even numbers are:  46
Even numbers are:  48
Odd numbers are:  15
Even numbers are:  50
Odd numbers are:  17
Even numbers are:  52
Odd numbers are:  19
Even numbers are:  54
Odd numbers are:  21
Even numbers are:  56
Odd numbers are:  23
Odd numbers are:  25
Even numbers are:  58
Odd numbers are:  27
Odd numbers are:  29
Odd numbers are:  31
Odd numbers are:  33
Odd numbers are:  35
Even numbers are:  60
Odd numbers are:  37
Odd numbers are:  39
Even numbers are:  62
Odd numbers are:  41
Odd numbers are:  43
Odd numbers are:  45
Odd numbers are:  47
Even numbers are:  64
Odd numbers are:  49
Odd numbers are:  51
Even numbers are:  66
Even numbers are:  68
Odd numbers are:  53
Odd numbers are:  55
Odd numbers are:  57
Odd numbers are:  59
Even numbers are:  70
Odd numbers are:  61
Even numbers are:  72
Odd numbers are:  63
Even numbers are:  74
Odd numbers are:  65
Even numbers are:  76
Odd numbers are:  67
Even numbers are:  78
Odd numbers are:  69
Even numbers are:  80
Odd numbers are:  71
Even numbers are:  82
Odd numbers are:  73
Even numbers are:  84
Odd numbers are:  75
Even numbers are:  86
Odd numbers are:  77
Even numbers are:  88
Even numbers are:  90
Even numbers are:  92
Odd numbers are:  79
Even numbers are:  94
Odd numbers are:  81
Even numbers are:  96
Odd numbers are:  83
Even numbers are:  98
Odd numbers are:  85
Even numbers are:  100
Odd numbers are:  87
Even numbers are:  102
Odd numbers are:  89
Even numbers are:  104
Odd numbers are:  91
Even numbers are:  106
Odd numbers are:  93
Even numbers are:  108
Odd numbers are:  95
Odd numbers are:  97
Even numbers are:  110
Even numbers are:  112
Odd numbers are:  99
Odd numbers are:  101
Even numbers are:  114
Odd numbers are:  103
Even numbers are:  116
Odd numbers are:  105
Even numbers are:  118
Odd numbers are:  107
Even numbers are:  120
Even numbers are:  122
Even numbers are:  124
Even numbers are:  126
Even numbers are:  128
Odd numbers are:  109
Even numbers are:  130
Odd numbers are:  111
Even numbers are:  132
Odd numbers are:  113
Even numbers are:  134
Even numbers are:  136
Even numbers are:  138
Even numbers are:  140
Odd numbers are:  115
Even numbers are:  142
Odd numbers are:  117
Even numbers are:  144
Odd numbers are:  119
Even numbers are:  146
Odd numbers are:  121
Even numbers are:  148
Odd numbers are:  123
Even numbers are:  150
Odd numbers are:  125
Even numbers are:  152
Odd numbers are:  127
Even numbers are:  154
Odd numbers are:  129
Even numbers are:  156
Odd numbers are:  131
Even numbers are:  158
Odd numbers are:  133
Even numbers are:  160
Odd numbers are:  135
Odd numbers are:  137
Odd numbers are:  139
Odd numbers are:  141
Even numbers are:  162
Even numbers are:  164
Odd numbers are:  143
Even numbers are:  166
Odd numbers are:  145
Even numbers are:  168
Odd numbers are:  147
Even numbers are:  170
Odd numbers are:  149
Even numbers are:  172
Odd numbers are:  151
Even numbers are:  174
Odd numbers are:  153
Even numbers are:  176
Odd numbers are:  155
Even numbers are:  178
Odd numbers are:  157
Odd numbers are:  159
Even numbers are:  180
Odd numbers are:  161
Even numbers are:  182
Even numbers are:  184
Odd numbers are:  163
Odd numbers are:  165
Even numbers are:  186
Odd numbers are:  167
Even numbers are:  188
Odd numbers are:  169
Even numbers are:  190
Odd numbers are:  171
Even numbers are:  192
Odd numbers are:  173
Even numbers are:  194
Odd numbers are:  175
Even numbers are:  196
Odd numbers are:  177
Even numbers are:  198
Odd numbers are:  179
Odd numbers are:  181
Odd numbers are:  183
Odd numbers are:  185
Odd numbers are:  187
Odd numbers are:  189
Odd numbers are:  191
Odd numbers are:  193
Odd numbers are:  195
Odd numbers are:  197
Odd numbers are:  199
Hello
Total execution time is:  0.046875
"""