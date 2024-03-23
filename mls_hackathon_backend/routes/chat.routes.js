const express=require('express');
const router=express.Router();
const getConversationBySenderId=require('../controller/getConversationBySenderId')
const saveConversation=require('../controller/saveConversation'); 
const saveUser = require('../controller/saveUser');
const { createUser, getUser } = require('../controller/create/user');


router.post('/create',saveConversation)
router.get('/:senderId',getConversationBySenderId)
router.post('/save',saveUser)
router.post('/register',createUser)
router.post('/login',getUser)


module.exports=router