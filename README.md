gpdsc2GNU 
=========

This is a little script to generate for a stm32Cubex generated software projects
a makefile. The project should be exported with Toolchain/IDE set to "Other Toolchains (GPDSC).

Missing support:
- Only stm32l476 with 1MByte Flash is supported
- GetConfiguration GUI looks a little bit strange

As the generation from stm32cubemx currently is a little bit experimantal (eg. startup 
files are not exported) I recommend to export it as well as SW4STM32 project. Further the 
generated xml file (ProjectName.gpdsc) does not represent a valid xml document wih respect to 
the schema (PACK.xsd). This kept me from using PyXB to generate bindings.


