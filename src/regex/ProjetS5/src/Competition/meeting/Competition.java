package Competition.meeting;


abstract class Competition  {

	protected    Match match;

	protected  final  List<Competitor> competitors;


	/**
	* auto gen docs
	**/
 	public    Competition(List<Competitor>) ;

	/**
	* auto gen docs
	* @return :void:
	**/
 	public  void  play() ;

	/**
	* auto gen docs
	* @return :void:
	**/
 	protected  void  play(List<Competitor>) ;

	/**
	* auto gen docs
	* @return :void:
	**/
 	protected  void  playMatch(Competitor c1,Competitor c2) ;

	/**
	* auto gen docs
	* @return :Map<Competitor,Integer>:
	**/
 	public  Map<Competitor,Integer>  ranking() {

		return new Map<Competitor,Integer>() ;
	}


}