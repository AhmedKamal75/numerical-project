import re
import numpy as np
import collections


def split_terms(equations_side):
    temp_terms = equations_side.split("+")
    for i in range(len(temp_terms)):
        temp_terms[i] = temp_terms[i].strip()
        if temp_terms[i][0] == "-":
            pass
        else:
            temp_terms[i] = "+" + temp_terms[i]

    terms = []
    for i in temp_terms:
        i.replace("–", "-")
        temps = i.split("-")
        for j in range(len(temps)):
            if len(temps[j]) < 1:
                continue
            temps[j] = temps[j].strip()
            if temps[j][0] != "+":
                temps[j] = "-" + temps[j]
            terms.append(temps[j])
    return terms


def extract_terms_b(equation_raw):
    if not str(equation_raw):
        return None

    (lhs, rhs) = equation_raw.split("=")
    lhs = lhs.strip()
    rhs = rhs.strip()

    lhs_terms = split_terms(lhs)
    if rhs != "0":
        for rhs_term in split_terms(rhs):
            if rhs_term[0] == "-":
                lhs_terms.append(rhs_term.replace("-", "+"))
            elif rhs_term[0] == "+":
                lhs_terms.append(rhs_term.replace("+", "-"))

    b = 0
    for term in lhs_terms:
        try:
            b = b + float(term)
            lhs_terms.remove(term)
        except:
            pass
    # print(lhs_terms)
    # print(b)

    return lhs_terms, b * -1.0


def terms_to_dic(terms):
    terms_and_coefficients = {}
    for term in terms:
        term = term.strip()
        sign = 1

        pattern = "^([+-])(\s)?([0-9]+(\.[0-9]+)?)?(\w)(\d+)?$"
        # group 1: sign
        # group 2: space
        # group 3: coefficient without sign
        # group 4: decimal part of coefficient
        # group 5: first part of the name
        # group 6: second part of the name
        result = re.search(pattern, term)
        if result.group(1) == "-":
            sign = -1

        coefficient = result.group(3)
        if coefficient is None:
            coefficient = 1
        if result.group(6) is None:
            name = result.group(5)
        else:
            name = result.group(5) + result.group(6)

        if name in terms_and_coefficients:
            terms_and_coefficients[name] = terms_and_coefficients[name] + float(coefficient) * float(sign)
        else:
            terms_and_coefficients[name] = float(coefficient) * float(sign)

    return terms_and_coefficients


class Equation:
    def __init__(self, equation_raw):
        (self._terms, self._b) = extract_terms_b(equation_raw)
        self._names__coefficients = terms_to_dic(self._terms)

        self._names = list(self._names__coefficients.keys())
        self._coefficients = list(self._names__coefficients.values())

    def define_new_names(self, name_set=None):
        if name_set is None:
            name_set = []

        for name in name_set:
            if name in self.names:
                continue
            else:
                self._names__coefficients[name] = 0

        self._names__coefficients = collections.OrderedDict(sorted(self._names__coefficients.items()))

    @property
    def coefficients(self):
        self._coefficients = list(self._names__coefficients.values())
        return self._coefficients

    @coefficients.setter
    def coefficients(self, coefficients):
        self._coefficients = coefficients

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, b):
        self._b = b

    @property
    def names(self):
        self._names = list(self._names__coefficients.keys())
        return self._names

    @names.setter
    def names(self, names):
        self._names = names


def get_A_b(str_equations=None):
    if str_equations is None:
        str_equations = []

    object_equations = []
    all_terms = []

    for i, equ_str in enumerate(str_equations):
        object_equations.append(Equation(equ_str))
        all_terms.extend(object_equations[i].names)
    all_terms = set(all_terms)

    for i, equ_obj in enumerate(object_equations):
        object_equations[i].define_new_names(all_terms)

    # for i, equ_obj in enumerate(object_equations):
    #     print(f"{object_equations[i].coefficients}   : {object_equations[i].b}")

    # if len(all_terms) != len(str_equations):
    #     print(f"fail number of unknowns = {len(all_terms)}, while number of equations = {len(str_equations)}")

    A = []
    b = []
    for equ_obj in object_equations:
        A.append(equ_obj.coefficients)
        b.append(equ_obj.b)

    return np.array(A), np.array([b]).transpose(), all_terms
