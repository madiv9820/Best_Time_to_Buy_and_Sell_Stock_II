from libcpp.vector cimport vector

cdef extern from "engine.hpp":
    cdef cppclass Solution:
        Solution() except + 
        int maxProfit(vector[int]& prices)

cdef class cppSolution:
    cdef Solution* thisPtr
    def __cinit__(self): self.thisPtr = new Solution()
    def __dealloc__(self): del self.thisPtr

    def maxProfit(self, prices):
        cdef vector[int] cpp_arr
        cdef int price

        for price in prices: cpp_arr.push_back(price)
        result = self.thisPtr.maxProfit(cpp_arr)
        return result