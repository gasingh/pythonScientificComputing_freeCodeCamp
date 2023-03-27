def paddedCalc(str0):
  """
    # 19:19 11/01/2023

    # ADDITION
    #str0 = "45 + 43"              # case1
    #str0 = "4509 + 43"            # case2
    #str0 = "45 + 43000"           # case3

    # SUBTRACTION
    #str0 = "45 - 43"              # case1
    #str0 = "4509 - 43"            # case2
    #str0 = "45 - 43000"           # case3
    """

  if "+" in str0:
    strLst = str0.split("+")
    strLst = list(map(lambda v: v.strip(), strLst))
    #print(strLst[0])
    #print(strLst[1])
    simplePad = " "
    charStr = "+"

    summ = str(sum([float(strLst[0]), float(strLst[1])]))[:-2]

    #"""
    # case 1
    if len(strLst[0]) == len(strLst[1]):
      str1Final = simplePad * 2 + strLst[0]
      str2Final = charStr + simplePad + strLst[1]
      str3Final = "-" * len(str1Final)
      #print(summ)
      str4Final = simplePad * (len(str3Final) - len(summ)) + summ
    #"""

    #"""
    # case 2
    if len(strLst[0]) > len(strLst[1]):
      str1Final = simplePad * 2 + strLst[0]
      #print(len(strLst[0])-len(strLst[1]),"__")
      str2Final = charStr + simplePad * (len(strLst[0]) - len(strLst[1]) +
                                         1) + strLst[1]
      str3Final = "-" * len(str1Final)
      str4Final = simplePad * (len(str3Final) - len(summ)) + summ
    #"""

    # case 3
    if len(strLst[0]) < len(strLst[1]):
      str1Final = simplePad * (len(strLst[1]) - len(strLst[0]) + 2) + strLst[0]
      #print(len(strLst[0])-len(strLst[1]),"__")
      str2Final = charStr + simplePad * (1) + strLst[1]
      str3Final = "-" * len(str1Final)
      str4Final = simplePad * (len(str3Final) - len(summ)) + summ

  elif "-" in str0:
    strLst = str0.split("-")
    strLst = list(map(lambda v: v.strip(), strLst))
    #print(strLst[0])
    #print(strLst[1])
    simplePad = " "
    charStr = "-"

    summ = str(float(strLst[0]) - float(strLst[1]))[:-2]

    #"""
    # case 1
    if len(strLst[0]) == len(strLst[1]):
      str1Final = simplePad * 2 + strLst[0]
      str2Final = charStr + simplePad + strLst[1]
      str3Final = "-" * len(str1Final)
      print(summ)
      str4Final = simplePad * (len(str3Final) - len(summ)) + summ
    #"""

    #"""
    # case 2
    if len(strLst[0]) > len(strLst[1]):
      str1Final = simplePad * 2 + strLst[0]
      #print(len(strLst[0])-len(strLst[1]),"__")
      str2Final = charStr + simplePad * (len(strLst[0]) - len(strLst[1]) +
                                         1) + strLst[1]
      str3Final = "-" * len(str1Final)
      str4Final = simplePad * (len(str3Final) - len(summ)) + summ
    #"""

    # case 3
    if len(strLst[0]) < len(strLst[1]):
      str1Final = simplePad * (len(strLst[1]) - len(strLst[0]) + 2) + strLst[0]
      #print(len(strLst[0])-len(strLst[1]),"__")
      str2Final = charStr + simplePad * (1) + strLst[1]
      str3Final = "-" * len(str1Final)
      str4Final = simplePad * (len(str3Final) - len(summ)) + summ

  # print(str1Final,str2Final,str3Final)
  """
    print(str1Final)
    print(str2Final)
    print(str3Final)
    print(str4Final)
    """

  return [str1Final, str2Final, str3Final, str4Final]


def operatorBasedProcedure(procStr, solutionBln):
  """
    printing and computation for a single str based on an identified operation
    12:31 08/01/2023
    """
  strCalcExpression = procStr
  calcLst = paddedCalc(strCalcExpression)
  #calcLst = list(map(float,calcLst))
  if solutionBln:
    #print(calcLst)
    return (calcLst)
  else:
    #print(calcLst)
    return (calcLst[:-1])


def arithmetic_computer(strCalcExpression, solutionBln=False):
  """
    Solution route decision and default checks.
    """
  return (operatorBasedProcedure(strCalcExpression, solutionBln))


strContatenateWithPadding = lambda v: "    ".join(
  v)  # we have a 4 spacing specification


def arithmetic_arranger(strCalcLst, solutionBln=False):
  """
    computes and illustrates many sums!
    13:20 08/01/2023
    """

  # COMPUTATION PRE-CHECKS
  proceedBln = None

  # CHECK 1
  """
    If there are too many problems supplied to the function. The limit is five,
    anything more will return: Error: Too many problems.
    """
  if len(strCalcLst) > 5:
    proceedBln = False
    return ("Error: Too many problems.")
  else:
    proceedBln = True
    pass

  # CHECK 2
  """
    The appropriate operators the function will accept are addition and 
    subtraction. Multiplication and division will return an error. Other 
    operators not mentioned in this bullet point will not need to be tested. 
    The error returned will be: Error: Operator must be '+' or '-'.
    """

  # operand checker
  def confirmOperand(string):
    import re
    regex = re.compile('[+-]')
    if (regex.search(string) != None):
      return (True)
    else:
      return (False)

  problemFoundCase2 = None
  for i, j in enumerate(strCalcLst):
    inputLst = j.split(" ")
    input1, operand, input2 = inputLst
    #print(operand,"....")
    if not confirmOperand(operand):
      problemFoundCase2 = True
  if problemFoundCase2 == True:
    proceedBln = False
    return ("Error: Operator must be '+' or '-'.")
  else:
    proceedBln = True

  # CHECK 3
  """
    Each number (operand) should only contain digits. Otherwise, the function 
    will return: Error: Numbers must only contain digits.
    """
  # input digit checker
  problemFoundCase3 = None

  def isfloat(num):
    try:
      float(num)
      return True
    except ValueError:
      return False

  for i, j in enumerate(strCalcLst):
    inputLst = j.split(" ")
    input1, operand, input2 = inputLst
    if not isfloat(input1):
      problemFoundCase3 = True
    elif not isfloat(input2):
      problemFoundCase3 = True
    else:
      pass
  if problemFoundCase3 == True:
    proceedBln = False
    return ("Error: Numbers must only contain digits.")
  else:
    proceedBln = True

  # CHECK 4
  """
    Each operand (aka number on each side of the operator) has a max of four 
    digits in width. Otherwise, the error string returned will be: 
    Error: Numbers cannot be more than four digits.
    """
  problemFoundCase4 = None
  for i, j in enumerate(strCalcLst):
    inputLst = j.split(" ")
    input1, operand, input2 = inputLst
    if len(input1) > 4:
      problemFoundCase4 = True
    elif len(input2) > 4:
      problemFoundCase4 = True
  if problemFoundCase4 == True:
    proceedBln = False
    return ("Error: Numbers cannot be more than four digits.")
  else:
    proceedBln = True

  # COMPUTATION STANDARD
  if proceedBln == True:
    # compute the stuff!
    streamMega = []
    for i, j in enumerate(strCalcLst):
      strCalcExpression = j
      outputStream = (arithmetic_computer(strCalcExpression, solutionBln))
      #print(outputStream)
      streamMega.append(outputStream)
      if solutionBln == True:
        stream1local, stream2local, stream3local, stream4local = outputStream
      else:
        stream1local, stream2local, stream3local = outputStream

    #print(streamMega)
    #print(list(zip(*streamMega)))
    streamMegaFlip = list(zip(*streamMega))
    strMega = ""
    for i, j in enumerate(streamMegaFlip):
      if i == len(streamMegaFlip) - 1:
        strMega = strMega + strContatenateWithPadding(j)
      else:
        strMega = strMega + strContatenateWithPadding(j) + "\n"
    return strMega
