import unittest.mock
from puncpy.classmodule import MyClass


class MyClassModuleTestCase(unittest.TestCase):
    # Tests for `classmodule.py`

    @unittest.mock.patch('puncpy.classmodule.word_tokenize', return_value=['This', 'is', 'my', 'own', 'invention'])
    @unittest.mock.patch('puncpy.classmodule.pos_tag', return_value=[('This', 'DT'), ('is', 'VBZ'), ('my', 'PRP$'), ('own', 'JJ'), ('invention', 'NN')])
    def test_tag_text(self, pos_tag_mock, word_tokenize_mock):
        # Arrange
        my_object = MyClass('This is my own invention')

        # Act
        result = my_object.tag_text()

        # Assert nltk.word_tokenize received correct input
        args, kwargs = word_tokenize_mock.call_args_list[0]
        assert args == ('This is my own invention',)

        # Assert nltk.pos_tag received correct input
        args, kwargs = pos_tag_mock.call_args_list[0]
        assert args == (['This', 'is', 'my', 'own', 'invention'],)

        # Assert tag_text output
        self.assertTrue(len(result) == 5)

