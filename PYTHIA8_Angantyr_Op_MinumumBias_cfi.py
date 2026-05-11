import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunesRun3ECM13p6TeV.PythiaCP2Settings_cfi import *

generator = cms.EDFilter("Pythia8ConcurrentGeneratorFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    AngantyrInitialState = cms.PSet(
        # Skip Pythia8::init() on LS re-entry (reuses the first-LS Angantyr
        # SigFit result in memory). Default is False (refit every LS).
        skipRefit = cms.untracked.bool(True),
    ),
    comEnergy = cms.double(9600.),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP2SettingsBlock,
        processParameters = cms.vstring(
            'SoftQCD:inelastic = on',
            'Beams:idA = 1000080160',
            'Beams:idB = 2212',
            'Beams:frameType = 2',
            'Beams:eA = 3400',
            'Beams:eB = 6800',
            'HeavyIon:mode = 1',
        ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CP2Settings',
                                    'processParameters'
                                    )
    )
)
