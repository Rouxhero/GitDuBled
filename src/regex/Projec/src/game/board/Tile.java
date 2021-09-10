package game.board;


 class Tile  {

	protected    int x;

	protected    int y;

	protected    Resources loot;

	protected    bool isEmpty;


	/**
	* auto gen docs
	**/
 	public    Tile(int x, int y) ;

	/**
	* auto gen docs
	* @return :int:
	**/
 	public  int  getX() {

		return 0;
	}

	/**
	* auto gen docs
	* @return :int:
	**/
 	public  int  getY() {

		return 0;
	}

	/**
	* auto gen docs
	* @return :Resources:
	**/
 	public  Resources  getResourcesOnHarvest() {

		return new Resources() ;
	}

	/**
	* auto gen docs
	* @return :int:
	**/
 	public  int  getUnitsOnTile() {

		return 0;
	}


}