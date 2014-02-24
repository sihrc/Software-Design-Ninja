from random_art import *


def evaluate_random_function_unit_tests():
  """ Tests the outputs of the required functions 'prod', 'sin_pi', and 'cos_pi' with x and y inputs 
      that range between -1 and 1.
      And tests the outputs using build_random_function() to check that the outpus are contained in 
      the range [-1, 1]
  """
  # Test 1: f = sin(pi * x), x = -1/2
  function_input_1_string = "sin(pi * x)"
  function_input_1 = ["sin_pi", ["x"]]
  x_1 = -1.0/2.0
  y_1 = 0.0
  e_output1 = -1.0

  # Test 2: f = y * cos(pi * x), x = 0, y = 0.5
  function_input_2_string = "y * cos(pi * x)"
  function_input_2 = ["prod", ["y"], ["cos_pi", ["x"]]]
  x_2 = 0.0
  y_2 = 0.5
  e_output2 = 0.5

  # Test 3: f = sin(pi * (cos(pi * x * y))), x = 1, y = 1/3
  function_input_3_string = "sin(pi * (cos(pi * x * y)))"
  function_input_3 = ["sin_pi", ["cos_pi", ["prod", ["x"], ["y"]]]]
  x_3 = 1.0
  y_3 = 1.0/3.0
  e_output3 = 1.0

  # Test 4: f = y, x = 0, y = -0.7
  function_input_4_string = 'y'
  function_input_4 = ["y"]
  x_4 = 0.0
  y_4 = -0.7
  e_output4 = -0.7

  # Actual output amino acid strands 
  a_output1 = evaluate_random_function(function_input_1, x_1, y_1)
  a_output2 = evaluate_random_function(function_input_2, x_2, y_2)
  a_output3 = evaluate_random_function(function_input_3, x_3, y_3)
  a_output4 = evaluate_random_function(function_input_4, x_4, y_4)

  test1_result = (e_output1 == a_output1)
  test2_result = (e_output2 == a_output2)
  test3_result = (e_output3 == a_output3)
  test4_result = (e_output4 == a_output4)

  if test1_result and test2_result and test3_result and test4_result:
      print '\nPASSED - evaluate_random_function_unit_tests()'
  else:
      print '\nFAILED - evaluate_random_function_unit_tests()'

  if not test1_result:
      print "\tTest 1 FAILED: \n\t\tInput function: " + function_input_1_string + "\n\t\tx: " + str(x_1) + "\n\t\ty: " + str(y_1) + "\n\t\tExpected Output: " + str(e_output1) + "\n\t\tActual Output: " + str(a_output1)
  if not test2_result:
      print "\tTest 2 FAILED: \n\t\tInput function: " + function_input_2_string + "\n\t\tx: " + str(x_2) + "\n\t\ty: " + str(y_2) + "\n\t\tExpected Output: " + str(e_output2) + "\n\t\tActual Output: " + str(a_output2)
  if not test3_result:
      print "\tTest 3 FAILED: \n\t\tInput function: " + function_input_3_string + "\n\t\tx: " + str(x_3) + "\n\t\ty: " + str(y_3) + "\n\t\tExpected Output: " + str(e_output3) + "\n\t\tActual Output: " + str(a_output3)
  if not test4_result:
      print "\tTest 4 FAILED: \n\t\tInput function: " + function_input_4_string + "\n\t\tx: " + str(x_4) + "\n\t\ty: " + str(y_4) + "\n\t\tExpected Output: " + str(e_output4) + "\n\t\tActual Output: " + str(a_output4)  

def remap_interval_unit_tests():

  input_val1 = 175
  input_range1 = [0, 350]
  output_range1 = [-1, 1]
  e_output1 = 0.0
  a_output1 = remap_interval(input_val1, input_range1[0], input_range1[1], output_range1[0], output_range1[1])

  input_val2 = 0
  input_range2 = [0, 350]
  output_range2 = [-1, 1]
  e_output2 = -1.0
  a_output2 = remap_interval(input_val2, input_range2[0], input_range2[1], output_range2[0], output_range2[1])

  input_val3 = 350
  input_range3 = [0, 350]
  output_range3 = [-1, 1]
  e_output3 = 1.0
  a_output3 = remap_interval(input_val3, input_range3[0], input_range3[1], output_range3[0], output_range3[1])

  input_val4 = 0
  input_range4 = [-1, 1]
  output_range4 = [0, 255]
  e_output4 = 127.5
  a_output4 = remap_interval(input_val4, input_range4[0], input_range4[1], output_range4[0], output_range4[1])

  test1_result = (e_output1 == a_output1)
  test2_result = (e_output2 == a_output2)
  test3_result = (e_output3 == a_output3)
  test4_result = (e_output4 == a_output4)

  if test1_result and test2_result and test3_result and test4_result:
      print '\nPASSED - remap_interval_unit_tests()'
  else:
      print '\nFAILED - remap_interval_unit_tests()'

  if not test1_result:
      print "\tTest 1 FAILED: \n\t\tInput value: " + str(input_val1) + "\n\t\tInput range: " + str(input_range1) + "\n\t\tOutput range: " + str(output_range1) + "\n\t\tExpected Output: " + str(e_output1) + "\n\t\tActual Output: " + str(a_output1)
  if not test2_result:
      print "\tTest 2 FAILED: \n\t\tInput value: " + str(input_val2) + "\n\t\tInput range: " + str(input_range2) + "\n\t\tOutput range: " + str(output_range2) + "\n\t\tExpected Output: " + str(e_output2) + "\n\t\tActual Output: " + str(a_output2)
  if not test3_result:
      print "\tTest 3 FAILED: \n\t\tInput value: " + str(input_val3) + "\n\t\tInput range: " + str(input_range3) + "\n\t\tOutput range: " + str(output_range3) + "\n\t\tExpected Output: " + str(e_output3) + "\n\t\tActual Output: " + str(a_output3)
  if not test4_result:
      print "\tTest 4 FAILED: \n\t\tInput value: " + str(input_val4) + "\n\t\tInput range: " + str(input_range4) + "\n\t\tOutput range: " + str(output_range4) + "\n\t\tExpected Output: " + str(e_output4) + "\n\t\tActual Output: " + str(a_output4)  



if __name__ == "__main__":
  print "\nCheck some of their random functions that they're building to give a quick glance:"
  for i in range(10):
    print build_random_function(0, 2)

  evaluate_random_function_unit_tests()

  remap_interval_unit_tests()

  print





