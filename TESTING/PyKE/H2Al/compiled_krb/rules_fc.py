# rules_fc.py

from pyke import contexts, pattern, fc_rule, knowledge_base

pyke_version = '1.1.1'
compiler_version = 1

def turn_on_lamp_when_door_opened(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('facts', 'door_opened', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('facts', 'turn_on_lamp',
                       (rule.pattern(0).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def populate(engine):
  This_rule_base = engine.get_create('rules')
  
  fc_rule.fc_rule('turn_on_lamp_when_door_opened', This_rule_base, turn_on_lamp_when_door_opened,
    (('facts', 'door_opened',
      (contexts.variable('door'),),
      False),),
    (contexts.variable('lamp'),))


Krb_filename = '..\\rules.krb'
Krb_lineno_map = (
    ((12, 16), (3, 3)),
    ((17, 18), (5, 5)),
)
