package t1.player;


/**
*
* @author Leo lvcdb, Adrien G
*/

abstract class Player implements Player {

	protected  boolean isRandomPlayer;

	protected  List<Character> listeChar;

	protected  Random ALEA;

	protected  int reward;

	protected  String name;

	protected  Board theboard;


	/**
	* //TODO
	*
	* @return :void:
	**/
 	public void Player(String name, int reward, Board board, boolean isRandom) ;

	/**
	* //TODO
	*
	* @param character : Character: 
	*
	* @return :void:
	**/
 	public void looseChar(Character character) ;

	/**
	* //TODO
	*
	* @param character : Character: 
	*
	* @return :void:
	**/
 	public void earnChar(Character character) ;

	/**
	* //TODO
	*
	* @return :String:
	**/
 	public String harvestTile() {

		return "";
	}

	/**
	* //TODO
	*
	* @return :String:
	**/
 	public String getName() {

		return "";
	}

	/**
	* //TODO
	*
	* @param theRess : Ressources: 
	*
	* @return :void:
	**/
 	private void increaseResources(Ressources theRess) ;

	/**
	* //TODO
	*
	* @return :String:
	**/
 	public String convertAllResources() {

		return "";
	}

	/**
	* //TODO
	*
	* @return :void:
	**/
 	private void cleanResources() ;

	/**
	* //TODO
	*
	* @param res : Ressources: 
	*
	* @return :void:
	**/
 	protected void convertResources(Ressources res) ;

	/**
	* //TODO
	*
	* @return :Tile:
	**/
 	public Tile getRandomTile() {

		return new Tile() ;
	}

	/**
	* //TODO
	*
	* @return :boolean:
	**/
 	public boolean isRandom() {

		return new boolean() ;
	}

	/**
	* //TODO
	*
	* @return :String:
	**/
 	public String doNothing() {

		return "";
	}

	/**
	* //TODO
	*
	* @return :String:
	**/
 	public String rewardCharacter() {

		return "";
	}

	/**
	* //TODO
	*
	* @return :int:
	**/
 	public int getNbSoldier() {

		return 0;
	}

	/**
	* //TODO
	*
	* @param character : Character: 
	*
	* @return :void:
	**/
 	public void looseFight(Character character) ;

	/**
	* //TODO
	*
	* @return :int:
	**/
 	public int getReward() {

		return 0;
	}

	/**
	* //TODO
	*
	* @param theRess : Ressources: 
	*
	* @return :int:
	**/
 	public int getNbRessources(Ressources theRess) {

		return 0;
	}

	/**
	* //TODO
	*
	* @return :String:
	**/
 	public String getCharacterString() {

		return "";
	}

	/**
	* //TODO
	*
	* @return :String:
	**/
 	public String toString() {

		return "";
	}

	/**
	* //TODO
	*
	* @return :String:
	**/
 	private String getRessourcesToString() {

		return "";
	}


}