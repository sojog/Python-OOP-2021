import os
import abc

from abc import ABC, abstractmethod

class AnswerList:
    def __init__(self, answers, correct_answer):
        self.answers = answers
        self.correct_answer  = correct_answer

class Question:
    def __init__(self, string_question, answers, points):
        self.string_question = string_question
        self.answers = answers
        self.points = points

    def __str__(self):
        return self.string_question + str(self.points)


class SingleAnswerQuestion(Question):
    
    def __init__(self,string_question,single_answer, points):
        super().__init__(string_question, single_answer, points)
        self.single_answer = single_answer

class MultipleAnswersQuestion(Question):
    def __init__(self,string_question,single_answer, points):
        super().__init__(string_question, single_answer, points)
        self.single_answer = single_answer


class QuestionCreator:
    def createQuestion(self, index, question_string, answers):
        if index < 10:
            return SingleAnswerQuestion(question_string, answers, 2)
        elif index < 20:
            return  SingleAnswerQuestion(question_string, answers, 3)
        else:
            return MultipleAnswersQuestion(question_string, answers, 5)

class Parser(ABC):
    @abstractmethod
    def read_questions(self):
        pass

class FileParser(Parser):
    def __init__(self):
        self._question_list = set()
    def read_questions(self, file_name):
        with open(file_name, "r") as file_handler:
            self.list_lines = file_handler.readlines()
        self._create_questions()
        return self._question_list
    def _questions_string(self):
        n = 6
        return [self.list_lines[i * n:(i + 1) * n] for i in range((len(self.list_lines) + n - 1) // n )] 

    def _create_questions(self):
         
        for (index, question) in enumerate(self._questions_string):
            q = question[0]
            first_answer = question[1]
            second_answer = question[2]
            third_answer = question[3]
            forth_answer = question[4]
            qc =  QuestionCreator()
            answers = [first_answer, second_answer, third_answer, forth_answer]
            question_object = qc.createQuestion(index, q, answers) 
            self._question_list.add(question_object)

from functools import reduce
# li = [1, 2, 3, 4, 5]
# sum = reduce((lambda x, y: x + y), li)
class FileParserUsingMap(FileParser):
    def _create_questions(self):
        qc =  QuestionCreator()
        question_creator = lambda index, obj : qc.createQuestion(obj[0], [obj[1], obj[2], obj[3], obj[4]], index) 
        self._question_list.update(list(map(question_creator, enumerate(self._question_list))))

class FileParserUsingReduce(FileParser):
    def _create_questions(self):
        qc =  QuestionCreator()
        for (index, list_question) in enumerate(self._questions_string()):
            question_creator_lambda =  lambda x: qc.createQuestion(index, x[0], [x[1], x[2], x[3], x[4]])
            question_object = reduce(question_creator_lambda, list_question)
            self._question_list.update(set(question_object))
            
class HarcodedParser(Parser):  
    def read_questions(self): 
          return "How are you?"      


file_name = "curs6.1.4-trivia-1.txt"

file_parser = FileParserUsingMap()
list_of_questions = file_parser.read_questions(file_name)



print(list_of_questions)
message = HarcodedParser()
print(message.read_questions())
