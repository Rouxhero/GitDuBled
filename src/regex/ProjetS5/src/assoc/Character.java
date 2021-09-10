package assoc;


abstract class Character  {

	protected    int gold;

	protected    Player Owner;

	protected    Tile position;


	/**
	* auto gen docs
	* @return :void:
	**/
 	public  void  getGold(int) ;

	/**
	* auto gen docs
	* @return :Tile:
	**/
 	public  Tile  getPosition() {

		return new Tile() ;
	}

	/**
	* auto gen docs
	* @return :Player:
	**/
 	public  Player  getOwner() {

		return new Player() ;
	}

	/**
	* auto gen docs
	* @return :void:
	**/
 	public  void  kill() ;

	/**
	* auto gen docs
	* @return :int:
	**/
 	protected  int  numberUnitsClaimed() {

		return 0;
	}


}