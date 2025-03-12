class InvertedInteger:


      def __init__(self, obj):
            self.object = obj


      # overwrite "print"
      def __str__(self):
            return "<" + str(self.object) + ">"


      # define "*"
      def __mul__(self,other):
            return InvertedInteger(self.object
                                              + other.object
                                              + self.object*other.object)
      

            # define "+" - Allows the program to support addition
      def __addition__(self,other):
            return InvertedInteger(self.object
                                              - other.object
                                              + self.object % other.object)
      
      
      def __check_positive_integer__(self, obj):
            return 

 #Validate the integer being entered (has to be a positive integer)
 #Negative integer would result in an error message
      

 #Supports a different type of multiplication


 #Supports a different type of addition