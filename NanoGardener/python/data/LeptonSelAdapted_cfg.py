
####################### Electrons ##################################

ElectronWP = {  
'Full2016': {

## ------------  

 'VetoObjWP' : { 
           'HLTsafe' : { 
                         'cuts' : { 
                               # Common cuts
                               'True' :
                                [
                                  'False'
                                  #'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                  #'electron_col[LF_idx]["cutBased_HLTPreSel"] == 1 ' ,
                                ] ,             
                                   },
                       } ,
                 } ,
  
 # ------------ 
 'FakeObjWP'  : {

           'HLTsafe' : { 
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                  [
                                   'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                   'electron_col[LF_idx]["cutBased_HLTPreSel"] == 1 ' ,
                                   'electron_col[LF_idx]["lostHits"] < 1',
                                  ] ,             
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                  [
                                    'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                    'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                  ] ,
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                  [
                                    'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                    'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                  ] ,
                                   },
                       } ,

                 } ,

 # ------------ 
 'TightObjWP' : {

         'cut_WP_Tight80X' : {
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                  [
                                    'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                    'electron_col[LF_idx]["cutBased_HLTPreSel"] == 1',
                                    'electron_col[LF_idx]["cutBased"] == 4', 
                                    'electron_col[LF_idx]["lostHits"] < 1',
                                  ] , 
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                  [
                                    'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                    'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                  ] ,
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                  [
                                    'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                    'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                  ] ,
                                  } ,
                         'tkSF':  { 
                                    '1-7' : 'LatinoAnalysis/Gardener/python/data/idiso/Full2016/egammaEffi.txt_EGM2D.root' ,
                                  } ,
                         'wpSF':  {
                                    '1-7' : 'LatinoAnalysis/Gardener/python/data/idiso/Full2016/electrons_cut_WP_Tight80X.txt' ,  
                                  } ,
                         'fakeW' : '/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/lowPtCorrected/36fb_ele_cut_WP_Tight80X/',
                             } ,


         'cut_WP_Tight80X_SS' : {
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                  [
                                    'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                    'electron_col[LF_idx]["cutBased_HLTPreSel"] == 1',
                                    'electron_col[LF_idx]["cutBased"] == 4',
                                    'electron_col[LF_idx]["lostHits"] < 1',
                                    'electron_col[LF_idx]["tightCharge"] == 2',
                                  ] ,
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                  [
                                    'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                    'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                  ] ,
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                  [
                                    'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                    'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                  ] ,
                                  } ,
                         'tkSF':  { 
                                    '1-7' : 'LatinoAnalysis/Gardener/python/data/idiso/Full2016/egammaEffi.txt_EGM2D.root' ,
                                  } ,
                         'wpSF':  {
                                    '1-7' : 'LatinoAnalysis/Gardener/python/data/idiso/Full2016/electrons_cut_WP_Tight80X_SS.txt' ,
                                  } ,
                         'fakeW' : '/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/lowPtCorrected/36fb_ele_cut_WP_Tight80X_SS/',
                             } ,


          'mva_80p_Iso2015':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["cutBased_HLTPreSel"] == 1',
                                     'electron_col[LF_idx]["mvaSpring16GP_WP80"]',
                                     'electron_col[LF_idx]["lostHits"] < 1',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                     'electron_col[LF_idx]["pfRelIso03_all"] < 0.0354',
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                     'electron_col[LF_idx]["pfRelIso03_all"] < 0.0646',
                                   ] ,
                                  } ,
                         'tkSF':  { 
                                    '1-7' : 'LatinoAnalysis/Gardener/python/data/idiso/Full2016/egammaEffi.txt_EGM2D.root' ,
                                  } ,
                         'wpSF':  {
                                    '1-7' : 'LatinoAnalysis/Gardener/python/data/idiso/Full2016/electrons_mva_80p_Iso2015.txt' ,
                                  } ,
                         'fakeW' : '/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/lowPtCorrected/36fb_ele_mva_80p_Iso2015/',
                              } ,
 
          'mva_80p_Iso2016':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["cutBased_HLTPreSel"] == 1',
                                     'electron_col[LF_idx]["mvaSpring16GP_WP80"]',
                                     'electron_col[LF_idx]["lostHits"] < 1',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                     'electron_col[LF_idx]["pfRelIso03_all"] < 0.05880',
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                     'electron_col[LF_idx]["pfRelIso03_all"] < 0.0571',
                                   ] ,
                                  } ,
                         'tkSF':  { 
                                    '1-7' : 'LatinoAnalysis/Gardener/python/data/idiso/Full2016/egammaEffi.txt_EGM2D.root' ,
                                  } ,
                         'wpSF':  {
                                    '1-7' : 'LatinoAnalysis/Gardener/python/data/idiso/Full2016/electrons_mva_80p_Iso2016.txt' ,
                                  } ,
                         'fakeW' : '/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/lowPtCorrected/36fb_ele_mva_80p_Iso2016/',
                              } ,
 
          'mva_90p_Iso2015':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["cutBased_HLTPreSel"] == 1',
                                     'electron_col[LF_idx]["mvaSpring16GP_WP90"]',
                                     'electron_col[LF_idx]["lostHits"] < 1',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                     'electron_col[LF_idx]["pfRelIso03_all"] < 0.0354',
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                     'electron_col[LF_idx]["pfRelIso03_all"] < 0.0646',
                                   ] ,
                                  } ,
                         'tkSF':  { 
                                    '1-7' : 'LatinoAnalysis/Gardener/python/data/idiso/Full2016/egammaEffi.txt_EGM2D.root' ,
                                  } ,
                         'wpSF':  {
                                    '1-7' : 'LatinoAnalysis/Gardener/python/data/idiso/Full2016/electrons_mva_90p_Iso2015.txt' ,
                                  } ,
                         'fakeW' : '/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/lowPtCorrected/36fb_ele_mva_90p_Iso2015/',
                              } ,
 
          'mva_90p_Iso2016':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["cutBased_HLTPreSel"] == 1',
                                     'electron_col[LF_idx]["mvaSpring16GP_WP90"]',
                                     'electron_col[LF_idx]["lostHits"] < 1',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                     'electron_col[LF_idx]["pfRelIso03_all"] < 0.05880',
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                     'electron_col[LF_idx]["pfRelIso03_all"] < 0.0571',
                                   ] ,
                                  } ,
                         'tkSF':  { 
                                    '1-7' : 'LatinoAnalysis/Gardener/python/data/idiso/Full2016/egammaEffi.txt_EGM2D.root' ,
                                  } ,
                         'wpSF':  {
                                    '1-7' : 'LatinoAnalysis/Gardener/python/data/idiso/Full2016/electrons_mva_90p_Iso2016.txt' ,
                                  } ,
                         'fakeW' : '/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/lowPtCorrected/36fb_ele_mva_90p_Iso2016/',
                              } ,
 
                  } ,
 
 # ------------ 
 'WgStarObjWP' : {

         'cut_WP_Tight80X' : {
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                  [
                                    'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                    #'electron_col[LF_idx]["cutBased_HLTPreSel"] == 1',
                                    #'electron_col[LF_idx]["cutBased"] == 4',
                                    'electron_col[LF_idx]["lostHits"] < 1',
                                    'electron_col[LF_idx]["convVeto"]',
                                    'electron_col[LF_idx]["tightCharge"] == 2',
                                  ] ,
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                  [
                                    'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                    'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                    'electron_col[LF_idx]["sieie"] < 0.00998',
                                    'electron_col[LF_idx]["deltaEtaSC"] < 0.00308',
                                    #'itree.std_vector_electron_dPhiIn"][LF_idx] < 0.0816',
                                    'electron_col[LF_idx]["hoe"] < 0.0414',
                                    'electron_col[LF_idx]["eInvMinusPInv"] < 0.0129',
                                    '(electron_col[LF_idx]["pfRelIso03_all"] - self.ConeOverlapPt(lepton_col, iLep)/electron_col[LF_idx]["pt"]) < 0.0588',                                  
                                  ] ,
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                  [
                                    'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                    'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                    'electron_col[LF_idx]["sieie"] < 0.0292',
                                    'electron_col[LF_idx]["deltaEtaSC"] < 0.00605',
                                    #'itree.std_vector_electron_dPhiIn"][LF_idx] < 0.0394',
                                    'electron_col[LF_idx]["hoe"] < 0.0641',
                                    'electron_col[LF_idx]["eInvMinusPInv"] < 0.0129',
                                    '(electron_col[LF_idx]["pfRelIso03_all"] - self.ConeOverlapPt(lepton_col, iLep)/electron_col[LF_idx]["pt"]) < 0.0571', 
                                  ] ,
                                  } ,
                             } ,

                 } ,
}


}


####################### Muons ######################################

MuonWP = {
'Full2016': {

## ------------  
 'VetoObjWP' : { 
      'HLTsafe' : {
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                 [
                                   'abs(muon_col[LF_idx]["eta"]) < 2.4' , 
                                   'muon_col[LF_idx]["pt"] > 10.0' ,
                                 ]
                                  } ,
                   }
               } ,

 # ------------ 
 'FakeObjWP'  : {

      'HLTsafe' : {
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                 [
                                   'abs(muon_col[LF_idx]["eta"]) < 2.4' , 
                                   'muon_col[LF_idx]["tightId"] == 1' ,
                                   'abs(muon_col[LF_idx]["dz"]) < 0.1' ,
                                   'muon_col[LF_idx]["pfRelIso04_all"] < 0.4',
                                   #'muon_col[LF_idx]["trackIso"]/muon_col[LF_idx]["pt"] < 0.4' ,
                                 ] ,
                                 # dxy for pT < 20 GeV
                                 'muon_col[LF_idx]["pt"] <= 20.0' :
                                 [
                                    'abs(muon_col[LF_idx]["dxy"]) < 0.01 ' ,
                                 ] ,
                                 # dxy for pT > 20 GeV
                                 'muon_col[LF_idx]["pt"] > 20.0' :
                                 [
                                    'abs(muon_col[LF_idx]["dxy"]) < 0.02 ' ,
                                 ] ,
                                  } ,

                       } ,
                 
                 } ,

 # ------------ 
 'TightObjWP' :  {

      'cut_Tight80x' : {
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                 [ 
                                   'abs(muon_col[LF_idx]["eta"]) < 2.4' ,
                                   'muon_col[LF_idx]["tightId"] == 1' ,
                                   'abs(muon_col[LF_idx]["dz"]) < 0.1' ,
                                   'muon_col[LF_idx]["pfRelIso04_all"] < 0.15',
                                   #'muon_col[LF_idx]["trackIso"]/muon_col[LF_idx]["pt"] < 0.4' ,
                                 ] ,
                                 # dxy for pT < 20 GeV
                                 'muon_col[LF_idx]["pt"] <= 20.0' :
                                 [
                                    'abs(muon_col[LF_idx]["dxy"]) < 0.01 ' ,
                                 ] ,
                                 # dxy for pT > 20 GeV
                                 'muon_col[LF_idx]["pt"] > 20.0' :
                                 [
                                    'abs(muon_col[LF_idx]["dxy"]) < 0.02 ' ,
                                 ] ,
                                  } ,
                         'tkSF':  { 
                                    '1-4' : 'LatinoAnalysis/Gardener/python/data/idiso/Full2016/trackerSF_Moriond17_MuoPOG_BCDEF.root' ,
                                    '5-7' : 'LatinoAnalysis/Gardener/python/data/idiso/Full2016/trackerSF_Moriond17_MuoPOG_GH.root' ,
                                  } ,
                         'idSF':  {
                                    '1-4' : [ 'LatinoAnalysis/Gardener/python/data/idiso/Full2016/Tight_Run2016BCDEF_PTvsETA_HWW.txt' ,
                                              'LatinoAnalysis/Gardener/python/data/idiso/Full2016/TightID_DY_madgraphLikeRun2016BCDEF_PTvsETA_HWW.txt' ] ,
                                    '5-7' : [ 'LatinoAnalysis/Gardener/python/data/idiso/Full2016/Tight_Run2016GH_PTvsETA_HWW.txt' ,
                                              'LatinoAnalysis/Gardener/python/data/idiso/Full2016/TightID_DY_madgraphLikeRun2016GH_PTvsETA_HWW.txt' ] ,
                                  } ,
                         'isoSF':  {
                                    '1-4' : [ 'LatinoAnalysis/Gardener/python/data/idiso/Full2016/ISOTight_Run2016BCDEF_PTvsETA_HWW.txt' ,
                                              'LatinoAnalysis/Gardener/python/data/idiso/Full2016/ISOTight_DY_madgraphLikeRun2016BCDEF_PTvsETA_HWW.txt' ] ,
                                    '5-7' : [ 'LatinoAnalysis/Gardener/python/data/idiso/Full2016/ISOTight_Run2016GH_PTvsETA_HWW.txt' ,
                                              'LatinoAnalysis/Gardener/python/data/idiso/Full2016/ISOTight_DY_madgraphLikeRun2016GH_PTvsETA_HWW.txt' ] , 
                                  } ,
                         'fakeW' : '/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/lowPtCorrected/36fb_muon/',

                       } ,

                 } ,

 # -------------
 'WgStarObjWP' : {
     'cut_Tight80x' : { 
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                 [
                                   'abs(muon_col[LF_idx]["eta"]) < 2.4' ,
                                   'muon_col[LF_idx]["tightId"] == 1' ,
                                   'abs(muon_col[LF_idx]["dz"]) < 0.1' ,
                                   '(muon_col[LF_idx]["pfRelIso04_all"] - self.ConeOverlapPt(lepton_col, iLep)/muon_col[LF_idx]["pt"]) < 0.15',
                                   ##'muon_col[LF_idx]["trackIso"]/muon_col[LF_idx]["pt"] < 0.4' ,
                                 ] ,
                                 # dxy for pT < 20 GeV
                                 'muon_col[LF_idx]["pt"] <= 20.0' :
                                 [
                                    'abs(muon_col[LF_idx]["dxy"]) < 0.01 ' ,
                                 ] ,
                                 # dxy for pT > 20 GeV
                                 'muon_col[LF_idx]["pt"] > 20.0' :
                                 [
                                    'abs(muon_col[LF_idx]["dxy"]) < 0.02 ' ,
                                 ] ,
                                  } ,
                       } ,
 
                 }, 
}

}



LepFilter_dict = {
   'Loose': 'isLoose',
   'Veto': 'isVeto',
   'WgStar': 'isWgs',
   'isLoose': 'FakeObjWP',
   'isVeto': 'VetoObjWP',
   'isWgs': 'WgStarObjWP'
}
