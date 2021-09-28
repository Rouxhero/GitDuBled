<p align="center">
	<img src="https://see.fontimg.com/api/renderfont4/ZV22x/eyJyIjoiZnMiLCJoIjo3NiwidyI6MTAwMCwiZnMiOjc2LCJmZ2MiOiIjM0Y5Njk4IiwiYmdjIjoiI0ZGRkZGRiIsInQiOjF9/VW1sIHRvIENvZGU/silvers-personal-use-regular.png" alt="Title">
</p>

# How to use !

# WSD synthaxe

```wsd
<package1Name>{

	[abstract]<class1>{
		[#|+|-] [static] [final] <Vartype> <Varname>
		[#|+|-] [static] [final] <Funcname>(<argType> <argName> , <..>)[:<return>]
	}
	[abstract]<class2>{
		[#|+|-] [static] [final] <Vartype> <Varname>
		[#|+|-] [static] [final] <Funcname>(<argType> <argName> , <..>)[:<return>]
	}
	[abstract]<class3>{
		[#|+|-] [static] [final] <Vartype> <Varname>
		[#|+|-] [static] [final] <Funcname>(<argType> <argName> , <..>)[:<return>]
	}

	<class1><|--<class2>
	<class1>*--<class3>
}

```

# Statu

## Done

### Docs

- return
- text

### read 

- package
- func
- var
- class
- link
- interface graphique
- Dossier Check

- Docs pour arguments @param :
`/**
	* auto gen docs
	* @param allCompetitor :List<Competitor>:
		* 
	**/
 	public    Competition(List<Competitor> allCompetitor) ;`
- auto gen docs -> insert text
- clear les \s de trop



## TODO 

- corriger open GUI linux : /usr/bin/thunar ~
- readme ??
- import *****

- faire code to teste - Nouvelle class first
