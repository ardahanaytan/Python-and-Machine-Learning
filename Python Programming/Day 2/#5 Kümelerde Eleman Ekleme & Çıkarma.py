l = ['gelecegi', 'yazanlar']
s = set(l)

dir(s)

s.add('ile')
s.add('gelecege_git')
s.add('ali')
s.add('ile')
s.remove('ali')
s.remove('ali')  #KeyError
s.discard('ali')
