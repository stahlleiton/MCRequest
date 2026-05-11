import FWCore.ParameterSet.Config as cms

_generator = cms.EDFilter("HijingGeneratorFilter",
                 rotateEventPlane = cms.bool(True),
                 frame = cms.string('CMS     '),
                 targ = cms.string('P       '),
                 izp = cms.int32(8),
                 bMin = cms.double(0),
                 izt = cms.int32(1),
                 proj = cms.string('A       '),
                 comEnergy = cms.double(9620.0),
                 iat = cms.int32(1),
                 bMax = cms.double(15),
                 iap = cms.int32(16)
)

from GeneratorInterface.Core.ExternalGeneratorFilter import ExternalGeneratorFilter
generator = ExternalGeneratorFilter(_generator)
