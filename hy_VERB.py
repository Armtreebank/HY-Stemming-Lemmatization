import re

class VerbParser:
  conjugations = {
    'infinitive': '-I',
    'infinitive-caus': '-IC',
    'infinitive-passive': '-IP',
    'infinitive-caus-passive': '-ICP',
    'infinitive-neg': '-IN',
    'infinitive-neg-caus': '-INC',
    'infinitive-neg-passive': '-INP',
    'infinitive-neg-caus-passive': '-INCP',
    'resultative_participle': '-RP',
    'resultative_participle-caus': '-RPC',
    'resultative_participle-passive': '-RPP',
    'resultative_participle-caus-passive': '-RPCP',
    'resultative_participle-neg': '-RPN',
    'resultative_participle-neg-caus': '-RPNC',
    'resultative_participle-neg-passive': '-RPNP',
    'resultative_participle-neg-caus-passive': '-RPNCP',
    'subject_participle': '-SP',
    'subject_participle-caus': '-SPC',
    'subject_participle-passive': '-SPP',
    'subject_participle-caus-passive': '-SPCP',
    'subject_participle-neg': '-SPN',
    'subject_participle-neg-caus': '-SPNC',
    'subject_participle-neg-passive': '-SPNP',
    'subject_participle-neg-caus-passive': '-SPNCP',
    'imperfective_converb': '-IC',
    'imperfective_converb-caus': '-ICC',
    'imperfective_converb-passive': '-ICP',
    'imperfective_converb-caus-passive': '-ICCP',
    'simultaneous_converb': '-SC',
    'simultaneous_converb-caus': '-SCC',
    'simultaneous_converb-passive': '-SCP',
    'simultaneous_converb-caus-passive': '-SCCP',
    'perfective_converb': '-PC',
    'perfective_converb-caus': '-PCC',
    'perfective_converb-passive': '-PCP',
    'perfective_converb-caus-passive': '-PCCP',
    'future_converb-i': '-FCI',
    'future_converb-i-caus': '-FCIC',
    'future_converb-i-passive': '-FCIP',
    'future_converb-i-caus-passive': '-FCICP',
    'future_converb-ii': '-FCII',
    'future_converb-ii-caus': '-FCIIC',
    'future_converb-ii-passive': '-FCIIP',
    'future_converb-ii-caus-passive': '-FCIICP',
    'connegative_converb': '-CC',
    'connegative_converb-caus': '-CCC',
    'connegative_converb-passive': '-CCP',
    'connegative_converb-caus-passive': '-CCCP',
    # +++++++++++++++
    'indicative-aorist-singular-first': '~IASF',
    'indicative-aorist-singular-second': '~IASS',
    'indicative-aorist-singular-third': '~IAST',
    'indicative-aorist-plural-first': '~IAPF',
    'indicative-aorist-plural-second': '~IAPS',
    'indicative-aorist-plural-third': '~IAPT',
    'indicative-aorist-caus-singular-first': '~IACSF',
    'indicative-aorist-caus-singular-second': '~IACSS',
    'indicative-aorist-caus-singular-third': '~IACST',
    'indicative-aorist-caus-plural-first': '~IACPF',
    'indicative-aorist-caus-plural-second': '~IACPS',
    'indicative-aorist-caus-plural-third': '~IACPT',
    'indicative-aorist-passive-singular-first': '~IAPSF',
    'indicative-aorist-passive-singular-second': '~IAPSS',
    'indicative-aorist-passive-singular-third': '~IAPST',
    'indicative-aorist-passive-plural-first': '~IAPPF',
    'indicative-aorist-passive-plural-second': '~IAPPS',
    'indicative-aorist-passive-plural-third': '~IAPPT',
    'indicative-aorist-caus-passive-singular-first': '~IACPSF',
    'indicative-aorist-caus-passive-singular-second': '~IACPSS',
    'indicative-aorist-caus-passive-singular-third': '~IACPST',
    'indicative-aorist-caus-passive-plural-first': '~IACPPF',
    'indicative-aorist-caus-passive-plural-second': '~IACPPS',
    'indicative-aorist-caus-passive-plural-third': '~IACPPT',
    'indicative-aorist-neg-singular-first': '~IANSF',
    'indicative-aorist-neg-singular-second': '~IANSS',
    'indicative-aorist-neg-singular-third': '~IANST',
    'indicative-aorist-neg-plural-first': '~IANPF',
    'indicative-aorist-neg-plural-second': '~IANPS',
    'indicative-aorist-neg-plural-third': '~IANPT',
    'indicative-aorist-neg-caus-singular-first': '~IANCSF',
    'indicative-aorist-neg-caus-singular-second': '~IANCSS',
    'indicative-aorist-neg-caus-singular-third': '~IANCST',
    'indicative-aorist-neg-caus-plural-first': '~IANCPF',
    'indicative-aorist-neg-caus-plural-second': '~IANCPS',
    'indicative-aorist-neg-caus-plural-third': '~IANCPT',
    'indicative-aorist-neg-passive-singular-first': '~IANPSF',
    'indicative-aorist-neg-passive-singular-second': '~IANPSS',
    'indicative-aorist-neg-passive-singular-third': '~IANPST',
    'indicative-aorist-neg-passive-plural-first': '~IANPPF',
    'indicative-aorist-neg-passive-plural-second': '~IANPPS',
    'indicative-aorist-neg-passive-plural-third': '~IANPPT',
    'indicative-aorist-neg-caus-passive-singular-first': '~IANCPSF',
    'indicative-aorist-neg-caus-passive-singular-second': '~IANCPSS',
    'indicative-aorist-neg-caus-passive-singular-third': '~IANCPST',
    'indicative-aorist-neg-caus-passive-plural-first': '~IANCPPF',
    'indicative-aorist-neg-caus-passive-plural-second': '~IANCPPS',
    'indicative-aorist-neg-caus-passive-plural-third': '~IANCPPT',
    'subjunctive-future-singular-first': '~SFSF',
    'subjunctive-future-singular-second': '~SFSS',
    'subjunctive-future-singular-third': '~SFST',
    'subjunctive-future-plural-first': '~SFPF',
    'subjunctive-future-plural-second': '~SFPS',
    'subjunctive-future-plural-third': '~SFPT',
    'subjunctive-future-caus-singular-first': '~SFCSF',
    'subjunctive-future-caus-singular-second': '~SFCSS',
    'subjunctive-future-caus-singular-third': '~SFCST',
    'subjunctive-future-caus-plural-first': '~SFCPF',
    'subjunctive-future-caus-plural-second': '~SFCPS',
    'subjunctive-future-caus-plural-third': '~SFCPT',
    'subjunctive-future-passive-singular-first': '~SFPSF',
    'subjunctive-future-passive-singular-second': '~SFPSS',
    'subjunctive-future-passive-singular-third': '~SFPST',
    'subjunctive-future-passive-plural-first': '~SFPPF',
    'subjunctive-future-passive-plural-second': '~SFPPS',
    'subjunctive-future-passive-plural-third': '~SFPPT',
    'subjunctive-future-caus-passive-singular-first': '~SFCPSF',
    'subjunctive-future-caus-passive-singular-second': '~SFCPSS',
    'subjunctive-future-caus-passive-singular-third': '~SFCPST',
    'subjunctive-future-caus-passive-plural-first': '~SFCPPF',
    'subjunctive-future-caus-passive-plural-second': '~SFCPPS',
    'subjunctive-future-caus-passive-plural-third': '~SFCPPT',
    'subjunctive-future-neg-singular-first': '~SFNSF',
    'subjunctive-future-neg-singular-second': '~SFNSS',
    'subjunctive-future-neg-singular-third': '~SFNST',
    'subjunctive-future-neg-plural-first': '~SFNPF',
    'subjunctive-future-neg-plural-second': '~SFNPS',
    'subjunctive-future-neg-plural-third': '~SFNPT',
    'subjunctive-future-neg-caus-singular-first': '~SFNCSF',
    'subjunctive-future-neg-caus-singular-second': '~SFNCSS',
    'subjunctive-future-neg-caus-singular-third': '~SFNCST',
    'subjunctive-future-neg-caus-plural-first': '~SFNCPF',
    'subjunctive-future-neg-caus-plural-second': '~SFNCPS',
    'subjunctive-future-neg-caus-plural-third': '~SFNCPT',
    'subjunctive-future-neg-passive-singular-first': '~SFNPSF',
    'subjunctive-future-neg-passive-singular-second': '~SFNPSS',
    'subjunctive-future-neg-passive-singular-third': '~SFNPST',
    'subjunctive-future-neg-passive-plural-first': '~SFNPPF',
    'subjunctive-future-neg-passive-plural-second': '~SFNPPS',
    'subjunctive-future-neg-passive-plural-third': '~SFNPPT',
    'subjunctive-future-neg-caus-passive-singular-first': '~SFNCPSF',
    'subjunctive-future-neg-caus-passive-singular-second': '~SFNCPSS',
    'subjunctive-future-neg-caus-passive-singular-third': '~SFNCPST',
    'subjunctive-future-neg-caus-passive-plural-first': '~SFNCPPF',
    'subjunctive-future-neg-caus-passive-plural-second': '~SFNCPPS',
    'subjunctive-future-neg-caus-passive-plural-third': '~SFNCPPT',
    'subjunctive-future_perfect-singular-first': '~SFP_SF',
    'subjunctive-future_perfect-singular-second': '~SFP_SS',
    'subjunctive-future_perfect-singular-third': '~SFP_ST',
    'subjunctive-future_perfect-plural-first': '~SFP_PF',
    'subjunctive-future_perfect-plural-second': '~SFP_PS',
    'subjunctive-future_perfect-plural-third': '~SFP_PT',
    'subjunctive-future_perfect-caus-singular-first': '~SFP_CSF',
    'subjunctive-future_perfect-caus-singular-second': '~SFP_CSS',
    'subjunctive-future_perfect-caus-singular-third': '~SFP_CST',
    'subjunctive-future_perfect-caus-plural-first': '~SFP_CPF',
    'subjunctive-future_perfect-caus-plural-second': '~SFP_CPS',
    'subjunctive-future_perfect-caus-plural-third': '~SFP_CPT',
    'subjunctive-future_perfect-passive-singular-first': '~SFP_PSF',
    'subjunctive-future_perfect-passive-singular-second': '~SFP_PSS',
    'subjunctive-future_perfect-passive-singular-third': '~SFP_PST',
    'subjunctive-future_perfect-passive-plural-first': '~SFP_PPF',
    'subjunctive-future_perfect-passive-plural-second': '~SFP_PPS',
    'subjunctive-future_perfect-passive-plural-third': '~SFP_PPT',
    'subjunctive-future_perfect-caus-passive-singular-first': '~SFP_CPSF',
    'subjunctive-future_perfect-caus-passive-singular-second': '~SFP_CPSS',
    'subjunctive-future_perfect-caus-passive-singular-third': '~SFP_CPST',
    'subjunctive-future_perfect-caus-passive-plural-first': '~SFP_CPPF',
    'subjunctive-future_perfect-caus-passive-plural-second': '~SFP_CPPS',
    'subjunctive-future_perfect-caus-passive-plural-third': '~SFP_CPPT',
    'subjunctive-future_perfect-neg-singular-first': '~SFP_NSF',
    'subjunctive-future_perfect-neg-singular-second': '~SFP_NSS',
    'subjunctive-future_perfect-neg-singular-third': '~SFP_NST',
    'subjunctive-future_perfect-neg-plural-first': '~SFP_NPF',
    'subjunctive-future_perfect-neg-plural-second': '~SFP_NPS',
    'subjunctive-future_perfect-neg-plural-third': '~SFP_NPT',
    'subjunctive-future_perfect-neg-caus-singular-first': '~SFP_NCSF',
    'subjunctive-future_perfect-neg-caus-singular-second': '~SFP_NCSS',
    'subjunctive-future_perfect-neg-caus-singular-third': '~SFP_NCST',
    'subjunctive-future_perfect-neg-caus-plural-first': '~SFP_NCPF',
    'subjunctive-future_perfect-neg-caus-plural-second': '~SFP_NCPS',
    'subjunctive-future_perfect-neg-caus-plural-third': '~SFP_NCPT',
    'subjunctive-future_perfect-neg-passive-singular-first': '~SFP_NPSF',
    'subjunctive-future_perfect-neg-passive-singular-second': '~SFP_NPSS',
    'subjunctive-future_perfect-neg-passive-singular-third': '~SFP_NPST',
    'subjunctive-future_perfect-neg-passive-plural-first': '~SFP_NPPF',
    'subjunctive-future_perfect-neg-passive-plural-second': '~SFP_NPPS',
    'subjunctive-future_perfect-neg-passive-plural-third': '~SFP_NPPT',
    'subjunctive-future_perfect-neg-caus-passive-singular-first': '~SFP_NCPSF',
    'subjunctive-future_perfect-neg-caus-passive-singular-second': '~SFP_NCPSS',
    'subjunctive-future_perfect-neg-caus-passive-singular-third': '~SFP_NCPST',
    'subjunctive-future_perfect-neg-caus-passive-plural-first': '~SFP_NCPPF',
    'subjunctive-future_perfect-neg-caus-passive-plural-second': '~SFP_NCPPS',
    'subjunctive-future_perfect-neg-caus-passive-plural-third': '~SFP_NCPPT',
    'conditional-future-singular-first': '~CFSF',
    'conditional-future-singular-second': '~CFSS',
    'conditional-future-singular-third': '~CFST',
    'conditional-future-plural-first': '~CFPF',
    'conditional-future-plural-second': '~CFPS',
    'conditional-future-plural-third': '~CFPT',
    'conditional-future-caus-singular-first': '~CFCSF',
    'conditional-future-caus-singular-second': '~CFCSS',
    'conditional-future-caus-singular-third': '~CFCST',
    'conditional-future-caus-plural-first': '~CFCPF',
    'conditional-future-caus-plural-second': '~CFCPS',
    'conditional-future-caus-plural-third': '~CFCPT',
    'conditional-future-passive-singular-first': '~CFPSF',
    'conditional-future-passive-singular-second': '~CFPSS',
    'conditional-future-passive-singular-third': '~CFPST',
    'conditional-future-passive-plural-first': '~CFPPF',
    'conditional-future-passive-plural-second': '~CFPPS',
    'conditional-future-passive-plural-third': '~CFPPT',
    'conditional-future-caus-passive-singular-first': '~CFCPSF',
    'conditional-future-caus-passive-singular-second': '~CFCPSS',
    'conditional-future-caus-passive-singular-third': '~CFCPST',
    'conditional-future-caus-passive-plural-first': '~CFCPPF',
    'conditional-future-caus-passive-plural-second': '~CFCPPS',
    'conditional-future-caus-passive-plural-third': '~CFCPPT',
    'conditional-future_perfect-singular-first': '~CFP_SF',
    'conditional-future_perfect-singular-second': '~CFP_SS',
    'conditional-future_perfect-singular-third': '~CFP_ST',
    'conditional-future_perfect-plural-first': '~CFP_PF',
    'conditional-future_perfect-plural-second': '~CFP_PS',
    'conditional-future_perfect-plural-third': '~CFP_PT',
    'conditional-future_perfect-caus-singular-first': '~CFP_CSF',
    'conditional-future_perfect-caus-singular-second': '~CFP_CSS',
    'conditional-future_perfect-caus-singular-third': '~CFP_CST',
    'conditional-future_perfect-caus-plural-first': '~CFP_CPF',
    'conditional-future_perfect-caus-plural-second': '~CFP_CPS',
    'conditional-future_perfect-caus-plural-third': '~CFP_CPT',
    'conditional-future_perfect-passive-singular-first': '~CFP_PSF',
    'conditional-future_perfect-passive-singular-second': '~CFP_PSS',
    'conditional-future_perfect-passive-singular-third': '~CFP_PST',
    'conditional-future_perfect-passive-plural-first': '~CFP_PPF',
    'conditional-future_perfect-passive-plural-second': '~CFP_PPS',
    'conditional-future_perfect-passive-plural-third': '~CFP_PPT',
    'conditional-future_perfect-caus-passive-singular-first': '~CFP_CPSF',
    'conditional-future_perfect-caus-passive-singular-second': '~CFP_CPSS',
    'conditional-future_perfect-caus-passive-singular-third': '~CFP_CPST',
    'conditional-future_perfect-caus-passive-plural-first': '~CFP_CPPF',
    'conditional-future_perfect-caus-passive-plural-second': '~CFP_CPPS',
    'conditional-future_perfect-caus-passive-plural-third': '~CFP_CPPT',
    'imperative-none-singular-second': '~INSS',
    'imperative-none-plural-second': '~INPS',
    'imperative-none-caus-singular-second': '~INCSS',
    'imperative-none-caus-plural-second': '~INCPS',
    'imperative-none-passive-singular-second': '~INPSS',
    'imperative-none-passive-plural-second': '~INPPS',
    'imperative-none-caus-passive-singular-second': '~INCPSS',
    'imperative-none-caus-passive-plural-second': '~INCPPS',
  }
  
  @staticmethod
  def elal( word ): 
    return word[:-2]
    
  @staticmethod
  def neg_ch( word_list ):
    return ['չ{}'.format(word) for word in word_list]
  
  def parse_word( self, type ):
    func_name =  self.conjugations.get(type)
    
    try:
      if func_name[:1] == '-':
        func = getattr(self, '{}0'.format(func_name[1:]))
      else:
        func = getattr(self, '{}1'.format(func_name[1:]))
    except:
      if 'neg' in type.split('-'):
        norm_func = '-'.join(filter(lambda x: True if x != 'neg' else False, type.split('-')))
        n_func_name =  self.conjugations.get(norm_func)
        try:
          if n_func_name[:1] == '-':
            norm_func = getattr(self, '{}0'.format(n_func_name[1:]))
          else:
            norm_func = getattr(self, '{}1'.format(n_func_name[1:]))
        except:
          return False
        else:
          word = self.neg_ch(norm_func())
          return {
            'word': word,
            'conj': type,
          }
      else:
        return False
    else:
      word = func()
      return {
        'word': word,
        'conj': type,
      }
  
  def parse( self, type=False ):
    if type:
      if not self.conjugations.get(type):
        raise KeyError
      else:
        parsed = self.parse_word(type)
        if parsed:
          return parsed
    else:
      c_arr = []
      for c in self.conjugations:
        parsed = self.parse_word(c)
        if parsed:
          c_arr.append(parsed)
      return c_arr
      
  def word_attr( self, attr ):
    for u, v in self.attr:
      if u == attr:
        return v
    return ''
    
  def word_attr_k( self, attr ):
    for u, v in self.attr:
      if attr == v:
        return True
    return False
    
  def word_attr_val( self, attr ):
    for u, v in self.attr:
      if attr in v:
        return v.split('=')[-1]
    return False

  def __init__( self, word, attr, **kwargs ):
    self.not_parsed_attr = attr
    self.word = word
    attr_list = re.split(r'\|(?=\|*)', attr[2:-2])
    for i in range(len(attr_list)-1, -1, -1):
      if attr_list[i] == '':
        attr_list[i+1] = '|' + attr_list[i+1]
        del attr_list[i]
    for i in range(len(attr_list)):
      attr_list[i] = '|' + attr_list[i]
    attributes = []
    for i in attr_list:
      attributes.append((i.count('|'), re.sub( r'\|', '', i)))
    self.attr = attributes
  
class VerbElParser(VerbParser):
  def indicative_aorist_st( self, ending, caus=False, passive=False ):
    root = self.elal(self.word)
    if root[-2:] == 'ցն':
      cut_end = 'ancn'
      stem = root[:-2]
    elif root[-1] == 'ն' or root[-1] == 'չ':
      cut_end = 'nch'
      stem = root[:-1]
    else:
      cut_end = None
      stem = root

    if passive and cut_end != 'ancn':
      p = 'վ'
    else:
      p = ''

    if caus:
      if cut_end == 'ancn':
        c = ''
      elif cut_end == 'nch':
        c = 'ցր'
      elif cut_end == None:
        c = 'եցր'

      if passive:
        if cut_end == 'ancn':
          c_p = ''
        elif cut_end == 'nch':
          c_p = 'ց'
        elif cut_end == None:
          c_p = 'եց'
      else:
        c_p = ''
    else:
      c = c_p = ''

    if cut_end == 'ancn':
      if passive:
        stem_c = 'ցվ'
      else:
        stem_c = 'ցր'

    if cut_end == 'nch':
      if not passive and not caus:
        end = [ending[1]]
      elif passive and not caus:
        end = ['']
      elif not passive and caus:
        end = [ending[0], ending[2]]
      else:
        end = [ending[2]]
    elif cut_end == 'ancn':
      if not passive and not caus:
        end = [stem_c + ending[2], stem_c + ending[0]]
      elif passive and not caus:
        end = [stem_c + ending[2]]
      elif not passive and caus:
        end = []
      else:
        end = []
    elif cut_end == None:
      if not passive and not caus:
        end = [ending[2]]
      elif passive and not caus:
        end = [ending[2]]
      elif not passive and caus:
        end = [ending[0]]
      else:
        end = [ending[2]]

    output = []
    for e in end:
      if e:
        output.append('{stem}{c}{p}{e}'.format(stem=stem, c=(c_p if c_p else c), p=p, e=e))
    return output
  
  def imperative_none_st( self, ending, caus=False, passive=False ):
    root = self.elal(self.word)
    stem = root
    if root[-2:] == 'ցն':
      stem = stem[:-2]
      cut_end = 'ancn'
    elif root[-1] == 'ն' or root[-1] == 'չ':
      stem = stem[:-1]
      cut_end = 'nch'
    else:
      cut_end = None

    if passive:
      p = 'վ'
    else:
      p = ''

    if caus:
      if cut_end == 'ancn':
        c = 'ցր'
      elif cut_end == 'nch':
        c = 'ցր'
      elif cut_end == None:
        c = 'եցր'

      if passive:
        if cut_end == 'ancn':
          c_p = 'եց'
        elif cut_end == 'nch':
          c_p = 'ց'
        elif cut_end == None:
          c_p = 'եց'
      else:
        c_p = ''
    else:
      c = c_p = ''

    if cut_end == 'ancn':
      end = ending
    elif cut_end == 'nch':
      end = ending
    elif cut_end == None:
      end = ending

    output = []
    if end:
      output.append('{stem}{c}{p}{e}'.format(stem=stem, c=(c_p if c_p else c), p=p, e=end))

    return output

  def standard_st( self, ending, caus=False, passive=False, conditional=False ):
    root = self.elal(self.word)
    if root[-2:] == 'ցն':
      cut_end = 'ancn'
    elif root[-1] == 'ն' or root[-1] == 'չ':
      cut_end = 'nch'
    else:
      cut_end = None
    stem = root

    if passive:
      p = 'վ'
    else:
      p = ''

    if caus:
      if cut_end == 'ancn':
        c = 'եցն'
      elif cut_end == 'nch':
        stem = stem[:-1]
        c = 'ցն'
      elif cut_end == None:
        c = 'եցն'

      if passive:
        if cut_end == 'ancn':
          c_p = 'եց'
        elif cut_end == 'nch':
          c_p = 'ց'
        elif cut_end == None:
          c_p = 'եց'
      else:
        c_p = ''
    else:
      c = c_p = ''

    if cut_end == 'ancn':
      if passive and not caus:
        end = ''
      else:
        end = ending
    elif cut_end == 'nch':
      if passive and not caus:
        end = ''
      else:
        end = ending
    elif cut_end == None:
      end = ending

    output = []
    if end:
      output.append('{cond}{stem}{c}{p}{e}'.format(cond='կ' if conditional else '', stem=stem, c=(c_p if c_p else c), p=p, e=end))

    return output

  def IASF1( self ):
    return self.indicative_aorist_st(['ի', 'ա', 'եցի'])
    
  def IASS1( self ):
    return self.indicative_aorist_st(['իր', 'ար', 'եցիր'])
    
  def IAST1( self ):
    return self.indicative_aorist_st(['եց', 'ավ', 'եց'])
      
  def IAPF1( self ):
    return self.indicative_aorist_st(['ինք', 'անք', 'եցինք'])
    
  def IAPS1( self ):
    return self.indicative_aorist_st(['իք', 'աք', 'եցիք'])
    
  def IAPT1( self ):
    return self.indicative_aorist_st(['ին', 'ան', 'եցին'])
    
  def IACSF1( self ):
    return self.indicative_aorist_st(['ի', 'ա', 'եցի'], caus=True)
    
  def IACSS1( self ):
    return self.indicative_aorist_st(['իր', 'ար', 'եցիր'], caus=True)
    
  def IACST1( self ):
    return self.indicative_aorist_st(['եց', 'ավ', 'եց'], caus=True)
      
  def IACPF1( self ):
    return self.indicative_aorist_st(['ինք', 'անք', 'եցինք'], caus=True)
    
  def IACPS1( self ):
    return self.indicative_aorist_st(['իք', 'աք', 'եցիք'], caus=True)
    
  def IACPT1( self ):
    return self.indicative_aorist_st(['ին', 'ան', 'եցին'], caus=True)
  
  def IAPSF1( self ):
    return self.indicative_aorist_st(['ի', 'ա', 'եցի'], passive=True)
    
  def IAPSS1( self ):
    return self.indicative_aorist_st(['իր', 'ար', 'եցիր'], passive=True)
    
  def IAPST1( self ):
    return self.indicative_aorist_st(['եց', 'ավ', 'եց'], passive=True)
      
  def IAPPF1( self ):
    return self.indicative_aorist_st(['ինք', 'անք', 'եցինք'], passive=True)
    
  def IAPPS1( self ):
    return self.indicative_aorist_st(['իք', 'աք', 'եցիք'], passive=True)
    
  def IAPPT1( self ):
    return self.indicative_aorist_st(['ին', 'ան', 'եցին'], passive=True)
    
  def IACPSF1( self ):
    return self.indicative_aorist_st(['ի', 'ա', 'եցի'], caus=True, passive=True)
    
  def IACPSS1( self ):
    return self.indicative_aorist_st(['իր', 'ար', 'եցիր'], caus=True, passive=True)
    
  def IACPST1( self ):
    return self.indicative_aorist_st(['եց', 'ավ', 'եց'], caus=True, passive=True)
      
  def IACPPF1( self ):
    return self.indicative_aorist_st(['ինք', 'անք', 'եցինք'], caus=True, passive=True)
    
  def IACPPS1( self ):
    return self.indicative_aorist_st(['իք', 'աք', 'եցիք'], caus=True, passive=True)
    
  def IACPPT1( self ):
    return self.indicative_aorist_st(['ին', 'ան', 'եցին'], caus=True, passive=True) 

  def SFSF1( self ):
    return self.standard_st('եմ')
    
  def SFSS1( self ):
    return self.standard_st('ես')
    
  def SFST1( self ):
    return self.standard_st('ի')
    
  def SFPF1( self ):
    return self.standard_st('ենք')
    
  def SFPS1( self ):
    return self.standard_st('եք')
    
  def SFPT1( self ):
    return self.standard_st('են')
    
  def SFCSF1( self ):
    return self.standard_st('եմ', caus=True)
    
  def SFCSS1( self ):
    return self.standard_st('ես', caus=True)
    
  def SFCST1( self ):
    return self.standard_st('ի', caus=True)
    
  def SFCPF1( self ):
    return self.standard_st('ենք', caus=True)
    
  def SFCPS1( self ):
    return self.standard_st('եք', caus=True)
    
  def SFCPT1( self ):
    return self.standard_st('են', caus=True)
    
  def SFPSF1( self ):
    return self.standard_st('եմ', passive=True)
    
  def SFPSS1( self ):
    return self.standard_st('ես', passive=True)
    
  def SFPST1( self ):
    return self.standard_st('ի', passive=True)
    
  def SFPPF1( self ):
    return self.standard_st('ենք', passive=True)
    
  def SFPPS1( self ):
    return self.standard_st('եք', passive=True)
    
  def SFPPT1( self ):
    return self.standard_st('են', passive=True)
    
  def SFCPSF1( self ):
    return self.standard_st('եմ', caus=True, passive=True)
    
  def SFCPSS1( self ):
    return self.standard_st('ես', caus=True, passive=True)
    
  def SFCPST1( self ):
    return self.standard_st('ի', caus=True, passive=True)
    
  def SFCPPF1( self ):
    return self.standard_st('ենք', caus=True, passive=True)
    
  def SFCPPS1( self ):
    return self.standard_st('եք', caus=True, passive=True)
    
  def SFCPPT1( self ):
    return self.standard_st('են', caus=True, passive=True)
  
  def SFP_SF1( self ):
    return self.standard_st('եի')
    
  def SFP_SS1( self ):
    return self.standard_st('եիր')
    
  def SFP_ST1( self ):
    return self.standard_st('եր')
    
  def SFP_PF1( self ):
    return self.standard_st('եինք')
    
  def SFP_PS1( self ):
    return self.standard_st('եիք')
    
  def SFP_PT1( self ):
    return self.standard_st('եին')
    
  def SFP_CSF1( self ):
    return self.standard_st('եի', caus=True)
    
  def SFP_CSS1( self ):
    return self.standard_st('եիր', caus=True)
    
  def SFP_CST1( self ):
    return self.standard_st('եր', caus=True)
    
  def SFP_CPF1( self ):
    return self.standard_st('եինք', caus=True)
    
  def SFP_CPS1( self ):
    return self.standard_st('եիք', caus=True)
    
  def SFP_CPT1( self ):
    return self.standard_st('եին', caus=True)
    
  def SFP_PSF1( self ):
    return self.standard_st('եի', passive=True)
    
  def SFP_PSS1( self ):
    return self.standard_st('եիր', passive=True)
    
  def SFP_PST1( self ):
    return self.standard_st('եր', passive=True)
    
  def SFP_PPF1( self ):
    return self.standard_st('եինք', passive=True)
    
  def SFP_PPS1( self ):
    return self.standard_st('եիք', passive=True)
    
  def SFP_PPT1( self ):
    return self.standard_st('եին', passive=True)
    
  def SFP_CPSF1( self ):
    return self.standard_st('եի', caus=True, passive=True)
    
  def SFP_CPSS1( self ):
    return self.standard_st('եիր', caus=True, passive=True)
    
  def SFP_CPST1( self ):
    return self.standard_st('եր', caus=True, passive=True)
    
  def SFP_CPPF1( self ):
    return self.standard_st('եինք', caus=True, passive=True)
    
  def SFP_CPPS1( self ):
    return self.standard_st('եիք', caus=True, passive=True)
    
  def SFP_CPPT1( self ):
    return self.standard_st('եին', caus=True, passive=True)
  
  def CFSF1( self ):
    return self.standard_st('եմ', conditional=True)
    
  def CFSS1( self ):
    return self.standard_st('ես', conditional=True)
    
  def CFST1( self ):
    return self.standard_st('ի', conditional=True)
    
  def CFPF1( self ):
    return self.standard_st('ենք', conditional=True)
    
  def CFPS1( self ):
    return self.standard_st('եք', conditional=True)
    
  def CFPT1( self ):
    return self.standard_st('են', conditional=True)
    
  def CFCSF1( self ):
    return self.standard_st('եմ', caus=True, conditional=True)
    
  def CFCSS1( self ):
    return self.standard_st('ես', caus=True, conditional=True)
    
  def CFCST1( self ):
    return self.standard_st('ի', caus=True, conditional=True)
    
  def CFCPF1( self ):
    return self.standard_st('ենք', caus=True, conditional=True)
    
  def CFCPS1( self ):
    return self.standard_st('եք', caus=True, conditional=True)
    
  def CFCPT1( self ):
    return self.standard_st('են', caus=True, conditional=True)
    
  def CFPSF1( self ):
    return self.standard_st('եմ', passive=True, conditional=True)
    
  def CFPSS1( self ):
    return self.standard_st('ես', passive=True, conditional=True)
    
  def CFPST1( self ):
    return self.standard_st('ի', passive=True, conditional=True)
    
  def CFPPF1( self ):
    return self.standard_st('ենք', passive=True, conditional=True)
    
  def CFPPS1( self ):
    return self.standard_st('եք', passive=True, conditional=True)
    
  def CFPPT1( self ):
    return self.standard_st('են', passive=True, conditional=True)
    
  def CFCPSF1( self ):
    return self.standard_st('եմ', caus=True, passive=True, conditional=True)
    
  def CFCPSS1( self ):
    return self.standard_st('ես', caus=True, passive=True, conditional=True)
    
  def CFCPST1( self ):
    return self.standard_st('ի', caus=True, passive=True, conditional=True)
    
  def CFCPPF1( self ):
    return self.standard_st('ենք', caus=True, passive=True, conditional=True)
    
  def CFCPPS1( self ):
    return self.standard_st('եք', caus=True, passive=True, conditional=True)
    
  def CFCPPT1( self ):
    return self.standard_st('են', caus=True, passive=True, conditional=True)
  
  def CFP_SF1( self ):
    return self.standard_st('եի', conditional=True)
    
  def CFP_SS1( self ):
    return self.standard_st('եիր', conditional=True)
    
  def CFP_ST1( self ):
    return self.standard_st('եր', conditional=True)
    
  def CFP_PF1( self ):
    return self.standard_st('եինք', conditional=True)
    
  def CFP_PS1( self ):
    return self.standard_st('եիք', conditional=True)
    
  def CFP_PT1( self ):
    return self.standard_st('եին', conditional=True)
    
  def CFP_CSF1( self ):
    return self.standard_st('եի', caus=True, conditional=True)
    
  def CFP_CSS1( self ):
    return self.standard_st('եիր', caus=True, conditional=True)
    
  def CFP_CST1( self ):
    return self.standard_st('եր', caus=True, conditional=True)
    
  def CFP_CPF1( self ):
    return self.standard_st('եինք', caus=True, conditional=True)
    
  def CFP_CPS1( self ):
    return self.standard_st('եիք', caus=True, conditional=True)
    
  def CFP_CPT1( self ):
    return self.standard_st('եին', caus=True, conditional=True)
    
  def CFP_PSF1( self ):
    return self.standard_st('եի', passive=True, conditional=True)
    
  def CFP_PSS1( self ):
    return self.standard_st('եիր', passive=True, conditional=True)
    
  def CFP_PST1( self ):
    return self.standard_st('եր', passive=True, conditional=True)
    
  def CFP_PPF1( self ):
    return self.standard_st('եինք', passive=True, conditional=True)
    
  def CFP_PPS1( self ):
    return self.standard_st('եիք', passive=True, conditional=True)
    
  def CFP_PPT1( self ):
    return self.standard_st('եին', passive=True, conditional=True)
    
  def CFP_CPSF1( self ):
    return self.standard_st('եի', caus=True, passive=True, conditional=True)
    
  def CFP_CPSS1( self ):
    return self.standard_st('եիր', caus=True, passive=True, conditional=True)
    
  def CFP_CPST1( self ):
    return self.standard_st('եր', caus=True, passive=True, conditional=True)
    
  def CFP_CPPF1( self ):
    return self.standard_st('եինք', caus=True, passive=True, conditional=True)
    
  def CFP_CPPS1( self ):
    return self.standard_st('եիք', caus=True, passive=True, conditional=True)
    
  def CFP_CPPT1( self ):
    return self.standard_st('եին', caus=True, passive=True, conditional=True)

  def INSS1( self ):
    return self.imperative_none_st('իր')
    
  def INPS1( self ):
    return self.imperative_none_st('եք')
    
  def INCSS1( self ):
    return self.imperative_none_st('ու', caus=True)
    
  def INCPS1( self ):
    return self.imperative_none_st('եք', caus=True)
  
  def INPSS1( self ):
    return self.imperative_none_st('իր', passive=True)
    
  def INPPS1( self ):
    return self.imperative_none_st('եք', passive=True)
    
  def INCPSS1( self ):
    return self.imperative_none_st('իր', caus=True, passive=True)
    
  def INCPPS1( self ):
    return self.imperative_none_st('եք', caus=True, passive=True)
    
class VerbAlParser(VerbParser):
  def indicative_aorist_st( self, ending, caus=False, passive=False ):
    root = self.elal(self.word)
    if root[-2:] == 'ան':
      cut_end = 'an'
      stem = root[:-2]
    elif root[-2:] == 'են':
      cut_end = 'en'
      stem = root[:-2]
    else:
      cut_end = None
      stem = root

    if passive:
      p = 'վ'
    else:
      p = ''

    if caus:
      if cut_end == 'an':
        c = 'ացր'
      elif cut_end == 'en':
        c = 'եցր'
      elif cut_end == None:
        c = 'ացր'

      if passive:
        if cut_end == 'an':
          c_p = 'աց'
        elif cut_end == 'en':
          c_p = 'եց'
        elif cut_end == None:
          c_p = 'աց'
      else:
        c_p = ''
    else:
      c = c_p = ''

    if cut_end == 'an':
      if not passive and not caus:
        end = [ending[1]]
      elif passive and not caus:
        end = ['']
      elif not passive and caus:
        end = [ending[0], ending[1]]
      else:
        end = [ending[0]]
    elif cut_end == 'en':
      if not passive and not caus:
        end = [ending[0]]
      elif passive and not caus:
        end = ['']
      elif not passive and caus:
        end = [ending[0], ending[1]]
      else:
        end = [ending[0]]
    elif cut_end == None:
      if not passive and not caus:
        end = [ending[2]]
      elif passive and not caus:
        end = ['']
      elif not passive and caus:
        end = [ending[0], ending[1]]
      else:
        end = [ending[0]]

    output = []
    for e in end:
      if e:
        output.append('{stem}{c}{p}{e}'.format(stem=stem, c=(c_p if c_p else c), p=p, e=e))
    return output
  
  def imperative_none_st( self, ending, caus=False, passive=False ):
    root = self.elal(self.word)
    if root[-2:] == 'ան':
      stem = root[:-2]
      cut_end = 'an'
    elif root[-2:] == 'են':
      stem = root[:-2]
      cut_end = 'en'
    else:
      cut_end = None
      stem = root

    if passive:
      p = 'վ'
    else:
      p = ''

    if caus:
      if cut_end == 'an':
        c = 'աց'
      elif cut_end == 'en':
        c = 'եց'
      elif cut_end == None:
        c = 'աց'

      if passive:
        if cut_end == 'an':
          c_p = 'աց'
        elif cut_end == 'en':
          c_p = 'եց'
        elif cut_end == None:
          c_p = 'աց'
      else:
        c_p = ''
    else:
      c = c_p = ''

    if cut_end == 'an':
      if not passive and not caus:
        end = ending[1]
      elif passive and not caus:
        end = ''
      elif not passive and caus:
        end = ending[0]
      else:
        end = ending[0]
    elif cut_end == 'en':
      if not passive and not caus:
        end = ending[2]
      elif passive and not caus:
        end = ''
      elif not passive and caus:
        end = ending[0]
      else:
        end = ending[0]
    elif cut_end == None:
      if not passive and not caus:
        end = ending[0]
      elif passive and not caus:
        end = ''
      elif not passive and caus:
        end = ending[0]
      else:
        end = ending[0]

    output = []
    if end:
      output.append('{stem}{c}{p}{e}'.format(stem=stem, c=(c_p if c_p else c), p=p, e=end))

    return output

  def standard_st( self, ending, caus=False, passive=False, conditional=False ):
    root = self.elal(self.word)
    if root[-2:] == 'ան':
      cut_end = 'an'
    elif root[-2:] == 'են':
      cut_end = 'en'
    else:
      cut_end = None
    stem = root

    if passive:
      p = 'վ'
    else:
      p = ''

    if caus:
      if cut_end == 'an':
        stem = stem[:-2]
        c = 'ացն'
      elif cut_end == 'en': 
        stem = stem[:-2]
        c = 'եցն'
      elif cut_end == None:
        c = 'ացն'

      if passive:
        if cut_end == 'an':
          c_p = 'աց'
        elif cut_end == 'en':
          c_p = 'եց'
        elif cut_end == None:
          c_p = 'աց'
      else:
        c_p = ''
    else:
      c = c_p = ''

    if cut_end == 'an':
      if not passive and not caus:
        end = ending
      elif passive and not caus:
        end = ''
      elif not passive and caus:
        end = ending
      else:
        end = ending
    elif cut_end == 'en':
      if not passive and not caus:
        end = ending
      elif passive and not caus:
        end = ''
      elif not passive and caus:
        end = ending
      else:
        end = ending
    elif cut_end == None:
      if not passive and not caus:
        end = ending
      elif passive and not caus:
        end = ''
      elif not passive and caus:
        end = ending
      else:
        end = ending

    output = []
    if end:
      output.append('{cond}{stem}{c}{p}{e}'.format(cond='կ' if conditional else '', stem=stem, c=(c_p if c_p else c), p=p, e=end))

    return output

  def IASF1( self ):
    return self.indicative_aorist_st(['եցա', 'ացա', 'ացի'])
    
  def IASS1( self ):
    return self.indicative_aorist_st(['եցար', 'ացար', 'ացիր'])
    
  def IAST1( self ):
    return self.indicative_aorist_st(['եցավ', 'ացավ', 'աց'])
      
  def IAPF1( self ):
    return self.indicative_aorist_st(['եցանք', 'ացանք', 'ացինք'])
    
  def IAPS1( self ):
    return self.indicative_aorist_st(['եցաք', 'ացաք', 'ացիք'])
    
  def IAPT1( self ):
    return self.indicative_aorist_st(['եցան', 'ացան', 'ացին'])
    
  def IACSF1( self ):
    return self.indicative_aorist_st(['եցի', 'ի'], caus=True)
    
  def IACSS1( self ):
    return self.indicative_aorist_st(['եցիր', 'իր'], caus=True)
    
  def IACST1( self ):
    return self.indicative_aorist_st(['եց', 'եց'], caus=True)
      
  def IACPF1( self ):
    return self.indicative_aorist_st(['եցինք', 'ինք'], caus=True)
    
  def IACPS1( self ):
    return self.indicative_aorist_st(['եցիք', 'իք'], caus=True)
    
  def IACPT1( self ):
    return self.indicative_aorist_st(['եցին', 'ին'], caus=True)
  
  def IAPSF1( self ):
    return self.indicative_aorist_st([], passive=True)
    
  def IAPSS1( self ):
    return self.indicative_aorist_st([], passive=True)
    
  def IAPST1( self ):
    return self.indicative_aorist_st([], passive=True)
      
  def IAPPF1( self ):
    return self.indicative_aorist_st([], passive=True)
    
  def IAPPS1( self ):
    return self.indicative_aorist_st([], passive=True)
    
  def IAPPT1( self ):
    return self.indicative_aorist_st([], passive=True)
    
  def IACPSF1( self ):
    return self.indicative_aorist_st(['եցի', 'ի'], caus=True, passive=True)
    
  def IACPSS1( self ):
    return self.indicative_aorist_st(['եցիր', 'իր'], caus=True, passive=True)
    
  def IACPST1( self ):
    return self.indicative_aorist_st(['եց', 'եց'], caus=True, passive=True)
      
  def IACPPF1( self ):
    return self.indicative_aorist_st(['եցինք', 'ինք'], caus=True, passive=True)
    
  def IACPPS1( self ):
    return self.indicative_aorist_st(['եցիք', 'իք'], caus=True, passive=True)
    
  def IACPPT1( self ):
    return self.indicative_aorist_st(['եցին', 'ին'], caus=True, passive=True) 

  def SFSF1( self ):
    return self.standard_st('ամ')
    
  def SFSS1( self ):
    return self.standard_st('աս')
    
  def SFST1( self ):
    return self.standard_st('ա')
    
  def SFPF1( self ):
    return self.standard_st('անք')
    
  def SFPS1( self ):
    return self.standard_st('աք')
    
  def SFPT1( self ):
    return self.standard_st('ան')
    
  def SFCSF1( self ):
    return self.standard_st('եմ', caus=True)
    
  def SFCSS1( self ):
    return self.standard_st('ես', caus=True)
    
  def SFCST1( self ):
    return self.standard_st('ի', caus=True)
    
  def SFCPF1( self ):
    return self.standard_st('ենք', caus=True)
    
  def SFCPS1( self ):
    return self.standard_st('եք', caus=True)
    
  def SFCPT1( self ):
    return self.standard_st('են', caus=True)
    
  def SFPSF1( self ):
    return self.standard_st('եմ', passive=True)
    
  def SFPSS1( self ):
    return self.standard_st('ես', passive=True)
    
  def SFPST1( self ):
    return self.standard_st('ի', passive=True)
    
  def SFPPF1( self ):
    return self.standard_st('ենք', passive=True)
    
  def SFPPS1( self ):
    return self.standard_st('եք', passive=True)
    
  def SFPPT1( self ):
    return self.standard_st('են', passive=True)
    
  def SFCPSF1( self ):
    return self.standard_st('եմ', caus=True, passive=True)
    
  def SFCPSS1( self ):
    return self.standard_st('ես', caus=True, passive=True)
    
  def SFCPST1( self ):
    return self.standard_st('ի', caus=True, passive=True)
    
  def SFCPPF1( self ):
    return self.standard_st('ենք', caus=True, passive=True)
    
  def SFCPPS1( self ):
    return self.standard_st('եք', caus=True, passive=True)
    
  def SFCPPT1( self ):
    return self.standard_st('են', caus=True, passive=True)
  
  def SFP_SF1( self ):
    return self.standard_st('այի')
    
  def SFP_SS1( self ):
    return self.standard_st('այիր')
    
  def SFP_ST1( self ):
    return self.standard_st('ար')
    
  def SFP_PF1( self ):
    return self.standard_st('այինք')
    
  def SFP_PS1( self ):
    return self.standard_st('այիք')
    
  def SFP_PT1( self ):
    return self.standard_st('ային')
    
  def SFP_CSF1( self ):
    return self.standard_st('եի', caus=True)
    
  def SFP_CSS1( self ):
    return self.standard_st('եիր', caus=True)
    
  def SFP_CST1( self ):
    return self.standard_st('եր', caus=True)
    
  def SFP_CPF1( self ):
    return self.standard_st('եինք', caus=True)
    
  def SFP_CPS1( self ):
    return self.standard_st('եիք', caus=True)
    
  def SFP_CPT1( self ):
    return self.standard_st('եին', caus=True)
    
  def SFP_PSF1( self ):
    return self.standard_st('եի', passive=True)
    
  def SFP_PSS1( self ):
    return self.standard_st('եիր', passive=True)
    
  def SFP_PST1( self ):
    return self.standard_st('եր', passive=True)
    
  def SFP_PPF1( self ):
    return self.standard_st('եինք', passive=True)
    
  def SFP_PPS1( self ):
    return self.standard_st('եիք', passive=True)
    
  def SFP_PPT1( self ):
    return self.standard_st('եին', passive=True)
    
  def SFP_CPSF1( self ):
    return self.standard_st('եի', caus=True, passive=True)
    
  def SFP_CPSS1( self ):
    return self.standard_st('եիր', caus=True, passive=True)
    
  def SFP_CPST1( self ):
    return self.standard_st('եր', caus=True, passive=True)
    
  def SFP_CPPF1( self ):
    return self.standard_st('եինք', caus=True, passive=True)
    
  def SFP_CPPS1( self ):
    return self.standard_st('եիք', caus=True, passive=True)
    
  def SFP_CPPT1( self ):
    return self.standard_st('եին', caus=True, passive=True)
  
  def CFSF1( self ):
    return self.standard_st('ամ', conditional=True)
    
  def CFSS1( self ):
    return self.standard_st('աս', conditional=True)
    
  def CFST1( self ):
    return self.standard_st('ա', conditional=True)
    
  def CFPF1( self ):
    return self.standard_st('անք', conditional=True)
    
  def CFPS1( self ):
    return self.standard_st('աք', conditional=True)
    
  def CFPT1( self ):
    return self.standard_st('ան', conditional=True)
    
  def CFCSF1( self ):
    return self.standard_st('եմ', caus=True, conditional=True)
    
  def CFCSS1( self ):
    return self.standard_st('ես', caus=True, conditional=True)
    
  def CFCST1( self ):
    return self.standard_st('ի', caus=True, conditional=True)
    
  def CFCPF1( self ):
    return self.standard_st('ենք', caus=True, conditional=True)
    
  def CFCPS1( self ):
    return self.standard_st('եք', caus=True, conditional=True)
    
  def CFCPT1( self ):
    return self.standard_st('են', caus=True, conditional=True)
    
  def CFPSF1( self ):
    return self.standard_st('եմ', passive=True, conditional=True)
    
  def CFPSS1( self ):
    return self.standard_st('ես', passive=True, conditional=True)
    
  def CFPST1( self ):
    return self.standard_st('ի', passive=True, conditional=True)
    
  def CFPPF1( self ):
    return self.standard_st('ենք', passive=True, conditional=True)
    
  def CFPPS1( self ):
    return self.standard_st('եք', passive=True, conditional=True)
    
  def CFPPT1( self ):
    return self.standard_st('են', passive=True, conditional=True)
    
  def CFCPSF1( self ):
    return self.standard_st('եմ', caus=True, passive=True, conditional=True)
    
  def CFCPSS1( self ):
    return self.standard_st('ես', caus=True, passive=True, conditional=True)
    
  def CFCPST1( self ):
    return self.standard_st('ի', caus=True, passive=True, conditional=True)
    
  def CFCPPF1( self ):
    return self.standard_st('ենք', caus=True, passive=True, conditional=True)
    
  def CFCPPS1( self ):
    return self.standard_st('եք', caus=True, passive=True, conditional=True)
    
  def CFCPPT1( self ):
    return self.standard_st('են', caus=True, passive=True, conditional=True)
  
  def CFP_SF1( self ):
    return self.standard_st('այի', conditional=True)
    
  def CFP_SS1( self ):
    return self.standard_st('այիր', conditional=True)
    
  def CFP_ST1( self ):
    return self.standard_st('ար', conditional=True)
    
  def CFP_PF1( self ):
    return self.standard_st('այինք', conditional=True)
    
  def CFP_PS1( self ):
    return self.standard_st('այիք', conditional=True)
    
  def CFP_PT1( self ):
    return self.standard_st('ային', conditional=True)
    
  def CFP_CSF1( self ):
    return self.standard_st('եի', caus=True, conditional=True)
    
  def CFP_CSS1( self ):
    return self.standard_st('եիր', caus=True, conditional=True)
    
  def CFP_CST1( self ):
    return self.standard_st('եր', caus=True, conditional=True)
    
  def CFP_CPF1( self ):
    return self.standard_st('եինք', caus=True, conditional=True)
    
  def CFP_CPS1( self ):
    return self.standard_st('եիք', caus=True, conditional=True)
    
  def CFP_CPT1( self ):
    return self.standard_st('եին', caus=True, conditional=True)
    
  def CFP_PSF1( self ):
    return self.standard_st('եի', passive=True, conditional=True)
    
  def CFP_PSS1( self ):
    return self.standard_st('եիր', passive=True, conditional=True)
    
  def CFP_PST1( self ):
    return self.standard_st('եր', passive=True, conditional=True)
    
  def CFP_PPF1( self ):
    return self.standard_st('եինք', passive=True, conditional=True)
    
  def CFP_PPS1( self ):
    return self.standard_st('եիք', passive=True, conditional=True)
    
  def CFP_PPT1( self ):
    return self.standard_st('եին', passive=True, conditional=True)
    
  def CFP_CPSF1( self ):
    return self.standard_st('եի', caus=True, passive=True, conditional=True)
    
  def CFP_CPSS1( self ):
    return self.standard_st('եիր', caus=True, passive=True, conditional=True)
    
  def CFP_CPST1( self ):
    return self.standard_st('եր', caus=True, passive=True, conditional=True)
    
  def CFP_CPPF1( self ):
    return self.standard_st('եինք', caus=True, passive=True, conditional=True)
    
  def CFP_CPPS1( self ):
    return self.standard_st('եիք', caus=True, passive=True, conditional=True)
    
  def CFP_CPPT1( self ):
    return self.standard_st('եին', caus=True, passive=True, conditional=True)

  def INSS1( self ):
    return self.imperative_none_st(['ա', 'ացիր', 'եցիր'])
    
  def INPS1( self ):
    return self.imperative_none_st(['ացեք', 'ացեք', 'եցեք'])
    
  def INCSS1( self ):
    return self.imperative_none_st(['րու'], caus=True)
    
  def INCPS1( self ):
    return self.imperative_none_st(['րեք'], caus=True)
  
  def INPSS1( self ):
    return self.imperative_none_st([''], passive=True)
    
  def INPPS1( self ):
    return self.imperative_none_st([''], passive=True)
    
  def INCPSS1( self ):
    return self.imperative_none_st(['իր'], caus=True, passive=True)
    
  def INCPPS1( self ):
    return self.imperative_none_st(['եք'], caus=True, passive=True)
    
class VerbParserFactory:
  parsers = {
    'ել' : VerbElParser,
    'ալ' : VerbAlParser,
  }
  
  @classmethod
  def parser( cls, word, attr, **kwargs ):
    type = re.split(r'\|(?=\|*)', attr[2:-2])[0][8:]
    if not type or not cls.parsers.get( type ):
      raise KeyError
    else:
      return cls.parsers.get( type )( word, attr )

if __name__ == '__main__':
  try:
    parser = VerbParserFactory.parser('կարդալ', '{{hy-conj-ալ|aor=վազեց}}')
    output = [parser.parse()]
  except Exception as E:
    print(E)
  else:
    file = open('verb.txt', 'w', encoding='utf-8')

    for i in output:
      for o in sorted(i, key=lambda x: x['conj']):
        file.write(o['conj'] + ': ' + str(o['word']) + '\n')
      file.write('\n'*4)
    file.close()
