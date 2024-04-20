pragma solidity ^0.8.12;

contract Supply{

struct material{
         uint ida;
	     string name;
	     string category;
	     string description;
	     string supplier;
	     string origin;
	     string productiondate;
	     string certificate;
	     string cost;
	     string quantity;
	     string types;
  }

struct product{
        uint id;
        string name;
        string category;
        string description;
        string specification;
        string unitofmeasurement;
        string manufacture_id;
        string types;
    }


material [] materials;

function addmaterials(
                uint ida,
                string memory namea,
                string memory categorya,
                string memory descriptiona,
                string memory suppliera,
                string memory origina,
                string memory productiondatea,
                string memory certificatea,
                string memory costa,
                string memory quantitya,
                string memory typea
            )
public{
	material memory e = material(
                            ida,
                            namea,
                            categorya,
                            descriptiona,
                            suppliera,
                            origina,
                            productiondatea,
                            certificatea,
                            costa,
                            quantitya,
                            typea
                );
	materials.push(e);
}

product [] products;

function addmproduct(
            uint ida,
            string memory namea,
            string memory categorya,
            string memory descriptiona,
            string memory specificationa,
            string memory unitofmeasurementa,
            string memory manufacture_ida,
            string memory typea
            )
public{
	product memory c=product(
	        ida,
	        namea,
	        categorya,
	        descriptiona,
	        specificationa,
	        unitofmeasurementa,
	        manufacture_ida,
	        typea
	);
	products.push(c);

} 


}
