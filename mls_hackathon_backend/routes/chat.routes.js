const express=require('express');
const router=express.Router();
const getConversationBySenderId=require('../controller/getConversationBySenderId')
const saveConversation=require('../controller/saveConversation'); 
const saveUser = require('../controller/saveUser');


router.post('/create',saveConversation)
router.get('/:senderId',getConversationBySenderId)
router.post('/save',saveUser)


module.exports=router