from pyke import knowledge_engine

my_engine = knowledge_engine.engine(__file__)

my_engine.activate('rules')

my_engine.get_kb('facts').dump_specific_facts()
