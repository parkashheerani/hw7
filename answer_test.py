import math
from math import pow, sqrt
import numpy as np
import answer

class TestAnswer():
    __correct__ = 0
    __total__ = 0

    @classmethod
    def setup_class(cls):
        print("Before")
        cls.__correct__ = 0
        cls.__total__ = 0

    @classmethod
    def teardown_class(cls):
        print(f"Score:{(cls.__correct__ / cls.__total__) * 100}%")

    def test_Q1_a(self):
        TestAnswer.__total__ += 1
        a,b,c,d = answer.import_method()
        assert (a == math.pi)
        TestAnswer.__correct__ += 1
    
    def test_Q1_b(self):
        TestAnswer.__total__ += 1
        a,b,c,d = answer.import_method()
        assert (b == pow(2, 3))
        TestAnswer.__correct__ += 1
    
    def test_Q1_c(self):
        TestAnswer.__total__ += 1
        a,b,c,d = answer.import_method()
        assert (c == (sqrt(25)))
        TestAnswer.__correct__ += 1
    
    def test_Q1_d(self):
        TestAnswer.__total__ += 1
        a,b,c,d = answer.import_method()
        A = np.array([[1, 2], [3, 4]])
        B = np.array([[5, 6], [7, 8]])
        result = d == np.dot(A, B)
        assert (result.all())
        TestAnswer.__correct__ += 1

    def test_Q2_normal_1(self):
        TestAnswer.__total__ += 1
        a = 12
        b = 6
        result = answer.commonFactors(a,b)
        assert (result == 4)
        TestAnswer.__correct__ += 1

    def test_Q2_normal_2(self):
        TestAnswer.__total__ += 1
        a = 25
        b = 30
        result = answer.commonFactors(a,b)
        assert (result == 2)
        TestAnswer.__correct__ += 1

    def test_Q2_normal_3(self):
        TestAnswer.__total__ += 1
        a = 3
        b = 6
        result = answer.commonFactors(a,b)
        assert (result == 2)
        TestAnswer.__correct__ += 1

    def test_Q2_normal_4(self):
        TestAnswer.__total__ += 1
        a = 100
        b = 50
        result = answer.commonFactors(a,b)
        assert (result == 6)
        TestAnswer.__correct__ += 1
    
    def test_Q3_normal_1(self):
        TestAnswer.__total__ += 1
        s = "abccbaacz"
        result = answer.repeatedCharacter(s)
        assert (result == "c")
        TestAnswer.__correct__ += 1

    def test_Q3_normal_2(self):
        TestAnswer.__total__ += 1
        s = "abcdd"
        result = answer.repeatedCharacter(s)
        assert (result == "d")
        TestAnswer.__correct__ += 1

    def test_Q3_normal_3(self):
        TestAnswer.__total__ += 1
        s = "acbdefghg"
        result = answer.repeatedCharacter(s)
        assert (result == "g")
        TestAnswer.__correct__ += 1

    def test_Q3_normal_4(self):
        TestAnswer.__total__ += 1
        s = "acbdefghkyturmfuira"
        result = answer.repeatedCharacter(s)
        assert (result == "a")
        TestAnswer.__correct__ += 1
    
    def test_Q4_normal_1(self):
        TestAnswer.__total__ += 1
        sentences = ["alice and bob love apple", "i think so too", "this is great thanks very much"]
        result = answer.mostWordsFound(sentences)
        assert (result == 6)
        TestAnswer.__correct__ += 1

    def test_Q4_normal_2(self):
        TestAnswer.__total__ += 1
        sentences = ["please wait", "continue to fight", "continue to win"]
        result = answer.mostWordsFound(sentences)
        assert (result == 3)
        TestAnswer.__correct__ += 1

    def test_Q4_normal_3(self):
        TestAnswer.__total__ += 1
        sentences = ["Hello", "No", "Yes"]
        result = answer.mostWordsFound(sentences)
        assert (result == 1)
        TestAnswer.__correct__ += 1

    def test_Q4_normal_4(self):
        TestAnswer.__total__ += 1
        sentences = ["Hello", "No", "Yes ok"]
        result = answer.mostWordsFound(sentences)
        assert (result == 2)
        TestAnswer.__correct__ += 1

    def test_Q4_normal_5(self):
        TestAnswer.__total__ += 1
        sentences = ["I love Stevens", "I love math and Python", "Yes Yes"]
        result = answer.mostWordsFound(sentences)
        assert (result == 5)
        TestAnswer.__correct__ += 1