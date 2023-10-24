// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;


contract Lottery {

    struct Player { 
        address wallet_address;
        string name;
        uint64 age;
    }

    mapping(address => Player) public addressToPlayer;


    event PlayerAdded(address indexed addr, string name, uint64 age);

    function addPlayer(address wallet_address, string memory name, uint64 age) public {
        Player memory new_player = Player(wallet_address, name, age);
        addressToPlayer[wallet_address] = new_player;

        emit PlayerAdded(wallet_address, name, age);
    }

    function removePlayer(address wallet_address) public {
        delete addressToPlayer[wallet_address];
    }
}