{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "b9e85c86",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "30\n"
     ]
    }
   ],
   "source": [
    "a=10\n",
    "b=20\n",
    "c=a+b\n",
    "print(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "5a2e9b92",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (2713850169.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"C:\\Users\\KIIT\\AppData\\Local\\Temp\\ipykernel_28604\\2713850169.py\"\u001b[1;36m, line \u001b[1;32m1\u001b[0m\n\u001b[1;33m    print\"helo python\"\u001b[0m\n\u001b[1;37m         ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "print\"helo python\"\n",
    "print(\"hello python\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "487a8769",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello\n"
     ]
    }
   ],
   "source": [
    "print(\"hello\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "cc9e8b92",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "100\n",
      "1000.0\n",
      "john\n"
     ]
    }
   ],
   "source": [
    "counter=100\n",
    "miles=1000.0\n",
    "name=\"john\"\n",
    "print(counter)\n",
    "print(miles)\n",
    "print(name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "e9a3c8b6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "100 1000.0 john\n"
     ]
    }
   ],
   "source": [
    "counter=100\n",
    "miles=1000.0\n",
    "name=\"john\"\n",
    "print(counter,miles,name)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "bfd37ae2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "100 1000.0 john\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "int"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "counter=100\n",
    "miles=1000.0\n",
    "name=\"john\"\n",
    "print(counter,miles,name)\n",
    "type(counter)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "244948ad",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "30 200 10 2 100000000000000000000\n"
     ]
    }
   ],
   "source": [
    "a=10\n",
    "b=20\n",
    "c=a+b\n",
    "d=a*b\n",
    "e=a%b\n",
    "f=int(b/a)\n",
    "g=a**b\n",
    "print(c,d,e,f,g)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "adf76ff8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['abcd', 1, 2.0, 34]\n",
      "1\n",
      "[1, 2.0]\n",
      "[1, 2.0, 34]\n",
      "[123, 'john', 123, 'john']\n"
     ]
    }
   ],
   "source": [
    "a=['abcd',1,2.0,34]\n",
    "b=[123,'john']\n",
    "print(a) #prints complete list\n",
    "print(a[0]) #prints first element of list\n",
    "print(a[1:3]) #prints elements starting from 2nd till 3rd\n",
    "print(a[1:]) #prints element starting from 2nd till end\n",
    "print(b*2) #prints the list twice"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "eab897c4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n",
      "[1, 2, 3, 4, 5, 6]\n",
      "['hi', 'hi', 'hi', 'hi']\n",
      "True\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "float"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "print(len([1,2,3]))\n",
    "print([1,2,3]+[4,5,6])\n",
    "print([\"hi\"]*4)\n",
    "print(3 in [1,2,3])\n",
    "type(a[2])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "43066fe3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "['abcd', 1, 2.0, 34, 1, 123, 'john']\n",
      "['abcd', 1, 2.0, 34, 1, 123]\n",
      "2\n",
      "['abcd', 1, 2.0, 34, 1, 123, 'kiit']\n",
      "['abcd', 1, 34, 1, 123, 'kiit']\n",
      "['kiit', 123, 1, 34, 1, 'abcd']\n",
      "['kiit', 123, 1, 34, 1, 'abcd', 'm', 'i', 'n']\n",
      "[2, 3, 4, 5, 8, 9]\n",
      "[9, 8, 5, 4, 3, 2]\n"
     ]
    }
   ],
   "source": [
    "a=['abcd',1,2.0,34]\n",
    "b=[123,'john']\n",
    "c=[2,5,4,3,8,9]\n",
    "d=[2,5,4,3,8,9]\n",
    "a.append(1)\n",
    "print(a.count(1))\n",
    "a.extend(b)\n",
    "print(a)\n",
    "a.pop()\n",
    "print(a)\n",
    "print(a.index(2.0))\n",
    "a.insert(6,'kiit')\n",
    "print(a)\n",
    "a.remove(2.0)\n",
    "print(a)\n",
    "a.reverse()\n",
    "print(a)\n",
    "a.extend('min')\n",
    "c.sort() #for ascending order\n",
    "d.sort(reverse=True) #for descending order\n",
    "print(a)\n",
    "print(c)\n",
    "print(d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "b4140e05",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Kathmandu\n",
      "devanshi\n",
      "{'Nepal': 'Kathmandu', 'Italy': 'Rome', 'England': 'London', 2: 'devanshi'}\n",
      "dict_keys(['Nepal', 'Italy', 'England', 2])\n",
      "dict_values(['Kathmandu', 'Rome', 'London', 'devanshi'])\n"
     ]
    }
   ],
   "source": [
    "a = {'Nepal': 'Kathmandu', 'Italy': 'Rome', 'England': 'London',2:'devanshi'}\n",
    "print (a['Nepal'])\n",
    "print(a[2])\n",
    "print(a)\n",
    "print(a.keys())\n",
    "print(a.values())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "510095f2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'1': 'rohan', '2': 'raj'}\n"
     ]
    }
   ],
   "source": [
    "a = {'Nepal': 'Kathmandu', 'Italy': 'Rome', 'England': 'London',2:'devanshi',3:{'1':'rohan','2':'raj'}} #dictionary inside dictionary\n",
    "print(a[3])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "24629e6e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'Name': 'devanshi', 'age': 20, 'Phone No': 937363738}\n"
     ]
    }
   ],
   "source": [
    "emp={1:{'Name':'devanshi','age':20,'Phone No':937363738},2:{'Name':'Vasudev','age':21,'Phone No':93746738}}\n",
    "print(emp[1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "cc2ec709",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('abcd', 756, 23.12, 'john')\n",
      "756\n",
      "(756, 23.12)\n",
      "(23.12, 'john')\n",
      "(12, 'ram', 12, 'ram')\n",
      "('abcd', 756, 23.12, 'john', 12, 'ram')\n"
     ]
    }
   ],
   "source": [
    "tuple=('abcd',756,23.12,'john')\n",
    "tup=(12,'ram')\n",
    "\n",
    "print(tuple)\n",
    "print(tuple[1])\n",
    "print(tuple[1:3])\n",
    "print(tuple[2:])\n",
    "print(tup*2)\n",
    "print(tuple+tup)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "e26c8153",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "['abcd', 756, 23.12, 'john', 756, 123, 'john']\n",
      "['abcd', 756, 23.12, 'john', 756, 123, 'john']\n",
      "2\n",
      "['abcd', 756, 23.12, 'john', 756, 123, 'kiit', 'john']\n"
     ]
    }
   ],
   "source": [
    "tuple=('abcd',756,23.12,'john')\n",
    "tup=(123,'john')\n",
    "a=list(tuple)\n",
    "b=list(tup)\n",
    "a.append(756)\n",
    "print(a.count(756))\n",
    "a.extend(b)\n",
    "print(a)\n",
    "print(a)\n",
    "print(a.index(23.12))\n",
    "a.insert(6,'kiit')\n",
    "print(a)\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
