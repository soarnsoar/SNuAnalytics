
plot['Wjets']  = {
                  'nameHR' : 'Wjets',
                  'isSignal' : 0,
                  'color': 921,
                  'isData'   : 0,
                  'samples'  : ['Wjets']
              }
plot['DY']  = {
                  'nameHR' : 'DY',
                  'isSignal' : 0,
                  'color': 418, 
                  'isData'   : 0,
                  'samples'  : ['DY']
              }

plot['top']  = {
                  'nameHR' : 'Top',
                  'isSignal' : 0,
                  'color': 400,   # kYellow
                  'isData'   : 0,                 
                  'samples'  : ['top']
              }

#plot['WWToLNuQQ']  = {
#                  'nameHR' : 'WWToLNuQQ',
#                  'isSignal' : 0,
#                  'color': 851,
#                  'isData'   : 0,
#                  'samples'  : ['WWToLNuQQ']
#              }


plot['ggHWWlnuqq_M700']  = {
                  'nameHR' : 'ggHWWlnuqq_M700',
                  'isSignal' : 1,
                  'isData'   : 0,
                  'color': 632,   
                  'samples'  : ['ggHWWlnuqq_M700'],
                  'scale'    : 30
}



plot['DATA']  = {
                  'nameHR' : 'DATA',
                  'isSignal' : 0,
                  'color': 1, 
                  'isData'   : 1 ,
                  'samples'  : ['DATA']
              }
legend['lumi'] = 'L = 35.9/fb'
#legend['lumi'] = 'Simulation'
legend['sqrt'] = '#sqrt{s} = 13 TeV'
