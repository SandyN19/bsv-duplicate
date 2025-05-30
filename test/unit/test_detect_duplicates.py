from src.util.detector import detect_duplicates
import pytest


# develop your test cases here

@pytest.mark.unit
def test_detect_duplicates():
    assert True

def test_less_than_two_articles():
    with pytest.raises(ValueError):
        detect_duplicates("")

def test_no_DOI():
    data = """
    @article{frattini2023requirements,
        title={Requirements quality research: a harmonized theory, evaluation, and roadmap},
        author={Frattini, Julian and Montgomery, Lloyd and Fischbach, Jannik and Mendez, Daniel and Fucci, Davide and Unterkalmsteiner, Michael},
        journal={Requirements Engineering},
        pages={1--14},
        year={2023},
        publisher={Springer},

    }

    @article{fernandez2017naming,
    title={Naming the pain in requirements engineering: Contemporary Problems, Causes, and Effects in Practice},
    author={M{e}ndez Fern{a}ndez, Daniel and Wagner, Stefan and Kalinowski, Marcos and Felderer, Michael and Mafra, Priscilla and Vetr{\`o}, Antonio and Conte, Tayana and Christiansson, M-T and Greer, Des and Lassenius, Casper and others},
    journal={Empirical software engineering},
    volume={22},
    number={5},
    pages={2298--2338},
    year={2017},
    publisher={Springer},

    }

    @article{mendez2017naming,
    title={Naming the pain in requirements engineering: Contemporary Problems, Causes, and Effects in Practice},
    author={M{e}ndez Fern{a}ndez, Daniel and Wagner, Stefan and Kalinowski, Marcos and Felderer, Michael and Mafra, Priscilla and Vetr{\`o}, Antonio and Conte, Tayana and Christiansson, M-T and Greer, Des and Lassenius, Casper and others},
    journal={Empirical software engineering},
    volume={22},
    number={5},
    pages={2298--2338},
    year={2017},
    publisher={Springer},
    doi={10.1007/s10664-016-9451-7}
    }
    """
    duplicates = detect_duplicates(data)
    assert len(duplicates) == 1

def test_with_DOI():
    data = """ @article{frattini2023requirements,
	title={Requirements quality research: a harmonized theory, evaluation, and roadmap},
	  author={Frattini, Julian and Montgomery, Lloyd and Fischbach, Jannik and Mendez, Daniel and Fucci, Davide and Unterkalmsteiner, Michael},
	  journal={Requirements Engineering},
	  pages={1--14},
	  year={2023},
	  publisher={Springer},
	  doi={10.1007/s00766-023-00405-y}
    }

    @article{fernandez2017naming,
    title={Naming the pain in requirements engineering: Contemporary Problems, Causes, and Effects in Practice},
    author={M{e}ndez Fern{a}ndez, Daniel and Wagner, Stefan and Kalinowski, Marcos and Felderer, Michael and Mafra, Priscilla and Vetr{\`o}, Antonio and Conte, Tayana and Christiansson, M-T and Greer, Des and Lassenius, Casper and others},
    journal={Empirical software engineering},
    volume={22},
    number={5},
    pages={2298--2338},
    year={2017},
    publisher={Springer},
    doi={10.1007/s10664-016-9451-7}
    }

    @article{mendez2017naming,
    title={Naming the pain in requirements engineering: Contemporary Problems, Causes, and Effects in Practice},
    author={M{e}ndez Fern{a}ndez, Daniel and Wagner, Stefan and Kalinowski, Marcos and Felderer, Michael and Mafra, Priscilla and Vetr{\`o}, Antonio and Conte, Tayana and Christiansson, M-T and Greer, Des and Lassenius, Casper and others},
    journal={Empirical software engineering},
    volume={22},
    number={5},
    pages={2298--2338},
    year={2017},
    publisher={Springer},
    doi={10.1007/s10664-016-9451-7}
    }"""
    duplicates = detect_duplicates(data)
    assert len(duplicates) == 1

"""
1. I copied the articles from github and followed my test case desgin documentation. 
"""