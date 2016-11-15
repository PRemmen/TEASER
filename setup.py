from setuptools import setup

setup(name='teaser',
      version='0.4.1',
      description='Tool for Energy Analysis and Simulation for Efficient Retrofit ',
      url='https://github.com/RWTH-EBC/TEASER',
      author='RWTH Aachen University, E.ON Energy Research Center, Institute of Energy Efficient Buildings and Indoor Climate',
      author_email='ebc-teaser@eonerc.rwth-aachen.de',
      license='MIT',
      packages=['teaser',
                'teaser.logic',
                'teaser.logic.archetypebuildings',
                'teaser.logic.archetypebuildings.bmvbs',
                'teaser.logic.archetypebuildings.bmvbs.custom',
                'teaser.logic.archetypebuildings.urbanrenet',
                'teaser.logic.buildingobjects',
                'teaser.logic.buildingobjects.boundaryconditions',
                'teaser.logic.buildingobjects.buildingphysics',
                'teaser.logic.buildingobjects.buildingsystems',
                'teaser.logic.simulation',
                'teaser.data',
                'teaser.data.bindings',
                'teaser.data.bindings.opengis',
                'teaser.data.bindings.opengis.citygml',
                'teaser.data.bindings.opengis.citygml.raw',
                'teaser.data.bindings.opengis.misc',
                'teaser.data.bindings.opengis.misc.raw',
                'teaser.data.bindings.opengis.raw',
                'teaser.data.bindings.schemas',
				'teaser.data.bindings.v_0_3_9',
				'teaser.data.bindings.v_0_4',
                'teaser.data.input',
                'teaser.data.input.inputdata',
                'teaser.data.output',
                'teaser.data.output.modelicatemplate',
                'teaser.data.output.modelicatemplate.AixLib',
                'teaser.data.output.modelicatemplate.Annex60',
                'teaser.data.output.texttemplate',
                'teaser.examples',
                'teaser.examples.simulation',
                'teaser.examples.verification',
				'teaser.examples.examplefiles',
				'teaser.examples.examplefiles.MelatenXML',
                'teaser.gui',
                'teaser.gui.controller',
                'teaser.gui.guihelp',
                'teaser.gui.guiimages',
                'teaser.gui.guiimages.OfficeBuildings',
                'teaser.gui.guiimages.Residentials',
                'tests'],
      package_data={'teaser.data.input.inputdata': ['*.xml'],
                    'teaser.data.output.modelicatemplate': ['package','package_order'],
                    'teaser.data.output.modelicatemplate.AixLib': ['AixLib_base','AixLib_model','AixLib_zone'],
                    'teaser.data.output.modelicatemplate.Annex60': ['Annex60_FourElements', 'Annex60_ThreeElements','Annex60_TwoElements'],
                    'teaser.data.output.texttemplate': ['ReadableBuilding'],
                    'teaser.data.bindings.schemas': ['*.xsd'],
                    'teaser.gui.guiimages': ['*.png'],
                    'teaser.gui.guiimages.OfficeBuildings': ['*.png'],
                    'teaser.gui.guiimages.Residentials': ['*.png'],
					'teaser.examples.examplefiles': ['*.teaserXML'],
					'teaser.examples.examplefiles.MelatenXML': ['*.xml']},
      classifiers = ['License :: OSI Approved :: MIT License'],
      setup_requires = ['mako', 'pyxb==1.2.4', 'pytest'],
      install_requires = ['mako', 'pyxb==1.2.4', 'pytest'])
