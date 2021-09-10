package game.game;


 class Player  {

	protected    HashMap<Resources,int> listeResources;

	protected    List<Character> listeCharacter;

	protected    List<Tile> territory;

	protected    int gold;


	/**
	* auto gen docs
	* @return :void:
	**/
 	public  void  deployCharac(Character character, Tile tile) ;

	/**
	* auto gen docs
	* @return :void:
	**/
 	public  void  harvestTerritory() ;

	/**
	* auto gen docs
	* @return :void:
	**/
 	public  void  feedCharac(Character character) ;

	/**
	* auto gen docs
	* @return :void:
	**/
 	public  void  endRound(Player player) ;

	/**
	* auto gen docs
	* @return :int:
	**/
 	public  int  convert(Resource resource) {

		return 0;
	}

	/**
	* auto gen docs
	* @return :int:
	**/
 	public  int  getPoints(Player player) {

		return 0;
	}

	/**
	* auto gen docs
	* @return :void:
	**/
 	public  void  rent(int amount) ;

	/**
	* auto gen docs
	* @return :int:
	**/
 	public  int  getGold(Player player) {

		return 0;
	}


}