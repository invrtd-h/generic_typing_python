
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASSIGN CLS_FN CLS_VAR COLON COMMA DOT EQ EXTENDS FALSE FN GENERATE ID IMPLIES LP1 LP2 LP3 NEQ NONE NOT OR PASS PRINTINFO PROGRAM_BEGIN PROGRAM_END RP1 RP2 RP3 R_ARROW STAR STATIC_FN S_COLON TRAIT TRAIT_OF TRUE VAR WS XOR program : PROGRAM_BEGIN S_COLON stmts PROGRAM_END S_COLON  program : WS  stmts : stmts stmt  stmts : stmt  stmt : trait_decl  stmt : print_stmt  stmt : generate_stmt  stmt : assign_stmt  stmt : S_COLON  trait_decl : TRAIT trait_id LP1 class_args RP1 COLON LP2 trait_decl_stmts RP2 S_COLON  trait_decl : TRAIT trait_id LP1 class_args RP1 EXTENDS unary_pred COLON LP2 trait_decl_stmts RP2 S_COLON  trait_id : ID  class_args : main_arg COMMA sub_args  class_args : main_arg  main_arg : ID  sub_args : necessary_args COMMA optional_args sub_args : necessary_args  sub_args : optional_args  necessary_args : necessary_args COMMA necessary_arg  necessary_args : necessary_arg  necessary_arg : ID  optional_args : optional_args COMMA optional_arg  optional_args : optional_arg  optional_arg : ID ASSIGN unary_pred trait_decl_stmts : trait_decl_stmts trait_decl_stmt  trait_decl_stmts : trait_decl_stmt  trait_decl_stmts : PASS S_COLON  trait_decl_stmt : FN COLON LP2 decl_fn_stmts RP2 S_COLON  trait_decl_stmt : VAR COLON LP2 decl_stmts RP2 S_COLON  trait_decl_stmt : CLS_FN COLON LP2 decl_cls_fn_stmts RP2 S_COLON  trait_decl_stmt : CLS_VAR COLON LP2 decl_stmts RP2 S_COLON  trait_decl_stmt : STATIC_FN COLON LP2 decl_static_fn_stmts RP2 S_COLON  trait_decl_stmt : error S_COLON  decl_fn_stmts : decl_fn_stmts decl_fn_stmt  decl_fn_stmts : decl_fn_stmt  decl_fn_stmt : fn_id LP1 pred_args RP1 S_COLON  decl_fn_stmt : fn_id LP1 pred_args RP1 R_ARROW unary_pred S_COLON  decl_fn_stmt : fn_id LP3 type_var_args RP3 LP1 pred_args RP1 S_COLON  decl_fn_stmt : fn_id LP3 type_var_args RP3 LP1 pred_args RP1 R_ARROW unary_pred S_COLON  decl_cls_fn_stmts : decl_cls_fn_stmts decl_cls_fn_stmt  decl_cls_fn_stmts : decl_cls_fn_stmt  decl_cls_fn_stmt : fn_id LP1 pred_args RP1 S_COLON  decl_cls_fn_stmt : fn_id LP1 pred_args RP1 R_ARROW unary_pred S_COLON  decl_cls_fn_stmt : fn_id LP3 type_var_args RP3 LP1 pred_args RP1 S_COLON  decl_cls_fn_stmt : fn_id LP3 type_var_args RP3 LP1 pred_args RP1 R_ARROW unary_pred S_COLON  fn_id : ID  pred_args : main_pred COMMA next_preds  pred_args : main_pred  main_pred : ID  next_preds : next_anonymous_necessary_preds COMMA next_anonymous_opt_preds COMMA STAR COMMA next_named_preds  next_preds : next_anonymous_necessary_preds COMMA next_anonymous_opt_preds COMMA STAR  next_preds : next_anonymous_necessary_preds COMMA next_anonymous_opt_preds next_preds : next_anonymous_necessary_preds COMMA STAR COMMA next_named_preds  next_preds : next_anonymous_necessary_preds COMMA STAR  next_preds : next_anonymous_necessary_preds  next_preds : next_anonymous_opt_preds COMMA STAR COMMA next_named_preds  next_preds : next_anonymous_opt_preds COMMA STAR  next_preds : next_anonymous_opt_preds  next_preds : STAR COMMA next_named_preds  next_preds : STAR  next_anonymous_necessary_preds : next_anonymous_necessary_preds COMMA next_anonymous_necessary_pred  next_anonymous_necessary_preds : next_anonymous_necessary_pred  next_anonymous_necessary_pred : unary_pred  next_anonymous_opt_preds : next_anonymous_opt_preds COMMA next_anonymous_opt_pred  next_anonymous_opt_preds : next_anonymous_opt_pred  next_anonymous_opt_pred : ASSIGN unary_pred  next_named_preds : next_named_preds COMMA next_named_pred  next_named_preds : next_named_pred  next_named_pred : next_named_necessary_pred  next_named_pred : next_named_opt_pred  next_named_necessary_pred : arg_name COLON unary_pred  next_named_opt_pred : arg_name COLON ASSIGN unary_pred  arg_name : ID  type_var_args : type_var_args COMMA type_var_arg  type_var_args : type_var_arg  type_var_arg : type_var_id  type_var_arg : type_var_id COLON unary_pred  type_var_id : ID  unary_pred : pred_name  unary_pred : unnamed_pred  unnamed_pred : pred_name LP3 args RP3  unnamed_pred : LP3 pred_expr RP3  unnamed_pred : TRAIT_OF LP1 var_expr RP1  unnamed_pred : NONE  pred_name : ID  pred_expr : pred_expr OR pred_expr_a  pred_expr : pred_expr_a  pred_expr_a : pred_expr_a AND pred_expr_b  pred_expr_a : pred_expr_b  pred_expr_b : NOT pred_expr_c  pred_expr_b : pred_expr_c  pred_expr_c : unary_pred  pred_expr_c : LP1 pred_expr RP1  var_expr : unary_pred DOT member_var_name  member_var_name : ID  decl_stmts : decl_stmts decl_stmt  decl_stmts : decl_stmt  decl_stmt : var_id S_COLON  decl_stmt : var_id COLON unary_pred S_COLON  decl_stmt : LP3 vars_id RP3 S_COLON  decl_stmt : LP3 vars_id RP3 COLON unary_pred S_COLON  vars_id : vars_id COMMA var_id  vars_id : var_id  var_id : ID  decl_static_fn_stmts : decl_static_fn_stmts decl_static_fn_stmt  decl_static_fn_stmts : decl_static_fn_stmt  decl_static_fn_stmt : static_fn_id LP1 next_preds RP1 S_COLON  decl_static_fn_stmt : static_fn_id LP1 next_preds RP1 R_ARROW unary_pred S_COLON  decl_static_fn_stmt : static_fn_id LP3 type_var_args RP3 LP1 next_preds RP1 S_COLON  decl_static_fn_stmt : static_fn_id LP3 type_var_args RP3 LP1 next_preds RP1 R_ARROW unary_pred S_COLON  decl_static_fn_stmt : static_fn_id LP1 RP1 S_COLON  decl_static_fn_stmt : static_fn_id LP1 RP1 R_ARROW unary_pred S_COLON  decl_static_fn_stmt : static_fn_id LP3 type_var_args RP3 LP1 RP1 S_COLON  decl_static_fn_stmt : static_fn_id LP3 type_var_args RP3 LP1 RP1 R_ARROW unary_pred S_COLON  static_fn_id : ID  print_stmt : PRINTINFO to_print S_COLON  generate_stmt : GENERATE to_print S_COLON  to_print : ID  to_print : boolean_expr  to_print : unnamed_pred  boolean_expr : boolean_expr OR boolean_expr_a  boolean_expr : boolean_expr_a  boolean_expr_a : boolean_expr_a XOR boolean_expr_b  boolean_expr_a : boolean_expr_b  boolean_expr_b : boolean_expr_b AND boolean_expr_c  boolean_expr_b : boolean_expr_c  boolean_expr_c : boolean_expr_c EQ boolean_expr_d  boolean_expr_c : boolean_expr_c NEQ boolean_expr_d  boolean_expr_c : boolean_expr_d  boolean_expr_d : NOT boolean_expr_e  boolean_expr_d : boolean_expr_e  boolean_expr_e : atomic_boolean_expr  boolean_expr_e : LP1 boolean_expr RP1  atomic_boolean_expr : constants  atomic_boolean_expr : unary_pred LP1 args RP1  atomic_boolean_expr : unary_pred IMPLIES unary_pred  atomic_boolean_expr : LP1 unary_pred EQ unary_pred RP1  atomic_boolean_expr : LP1 unary_pred NEQ unary_pred RP1  constants : TRUE  constants : FALSE  args : args COMMA arg  args : arg  arg : ID  assign_stmt : names ASSIGN assign_expr S_COLON  names : names COMMA name  names : name  name : ID  assign_expr : names ASSIGN assign_expr  assign_expr : names '
    
_lr_action_items = {'PROGRAM_BEGIN':([0,],[2,]),'WS':([0,],[3,]),'$end':([1,3,45,],[0,-2,-1,]),'S_COLON':([2,4,5,6,7,8,9,10,11,16,17,18,19,22,23,24,25,26,31,32,33,34,36,37,38,40,41,42,47,58,59,60,67,70,71,72,73,77,78,82,89,92,93,94,96,98,101,106,110,111,123,124,132,138,145,155,168,170,179,180,184,190,194,195,199,209,210,218,227,236,238,252,258,271,274,276,284,286,288,296,307,308,309,311,],[4,5,-9,5,-4,-5,-6,-7,-8,-146,-147,45,-3,47,-118,-119,-120,-122,-84,-124,-126,-129,-131,-132,-134,-139,-140,70,-116,-79,-80,-85,-130,-117,-149,98,-145,-121,-123,-82,-133,-125,-127,-128,-136,-144,-81,-83,-135,-148,-137,-138,147,153,155,-10,186,-104,199,200,208,212,215,216,-11,232,233,239,246,253,256,273,277,285,287,289,297,299,301,305,312,313,314,315,]),'TRAIT':([4,5,6,7,8,9,10,11,19,47,70,98,155,199,],[12,-9,12,-4,-5,-6,-7,-8,-3,-116,-117,-144,-10,-11,]),'PRINTINFO':([4,5,6,7,8,9,10,11,19,47,70,98,155,199,],[13,-9,13,-4,-5,-6,-7,-8,-3,-116,-117,-144,-10,-11,]),'GENERATE':([4,5,6,7,8,9,10,11,19,47,70,98,155,199,],[14,-9,14,-4,-5,-6,-7,-8,-3,-116,-117,-144,-10,-11,]),'ID':([4,5,6,7,8,9,10,11,12,13,14,19,28,30,35,43,44,46,47,48,49,50,54,57,61,64,65,66,68,69,70,83,84,90,91,97,98,100,102,107,113,127,128,129,155,156,157,158,159,160,162,163,166,167,169,171,172,174,175,176,181,182,183,185,186,187,191,192,193,196,197,198,199,211,225,228,230,231,232,233,234,239,240,241,243,246,247,249,253,254,255,256,257,270,273,277,279,280,281,282,285,287,289,295,297,298,299,300,301,302,303,305,306,312,313,314,315,],[17,-9,17,-4,-5,-6,-7,-8,21,23,23,-3,60,60,60,17,17,76,-116,60,60,81,60,60,60,60,60,60,81,60,-117,60,60,60,60,17,-144,119,81,122,60,119,143,60,-10,165,170,165,170,178,165,-35,170,-97,170,165,-41,170,178,-106,-34,203,207,-96,-98,60,-40,203,207,-105,60,207,-11,170,60,60,207,60,-99,-100,60,-111,60,60,269,-36,60,203,-42,60,203,-107,60,60,-101,-112,269,269,269,60,-37,-43,-108,60,-113,60,-38,60,-44,60,269,-109,60,-114,-39,-45,-110,]),'PROGRAM_END':([5,6,7,8,9,10,11,19,47,70,98,155,199,],[-9,18,-4,-5,-6,-7,-8,-3,-116,-117,-144,-10,-11,]),'LP3':([13,14,23,27,28,30,35,48,49,54,57,58,60,61,64,65,66,69,83,84,90,91,113,129,157,159,164,165,166,167,173,174,177,178,185,186,187,197,225,228,231,232,233,234,240,241,247,254,257,270,273,282,295,298,300,302,306,],[28,28,-85,50,28,28,28,28,28,28,28,50,-85,28,28,28,28,28,28,28,28,28,28,28,169,169,183,-46,169,-97,193,169,198,-115,-96,-98,28,28,28,28,28,-99,-100,28,28,28,28,28,28,28,-101,28,28,28,28,28,28,]),'TRAIT_OF':([13,14,28,30,35,48,49,54,57,61,64,65,66,69,83,84,90,91,113,129,187,197,225,228,231,234,240,241,247,254,257,270,282,295,298,300,302,306,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'NONE':([13,14,28,30,35,48,49,54,57,61,64,65,66,69,83,84,90,91,113,129,187,197,225,228,231,234,240,241,247,254,257,270,282,295,298,300,302,306,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'NOT':([13,14,28,30,48,49,57,64,65,66,83,84,],[35,35,54,35,35,35,54,35,35,35,54,54,]),'LP1':([13,14,20,21,23,25,27,28,29,30,31,35,39,48,49,54,57,58,59,60,63,64,65,66,82,83,84,101,106,164,165,173,177,178,229,237,245,],[30,30,46,-12,-85,-80,-79,57,61,30,-84,30,68,30,30,57,57,-79,-80,-85,68,30,30,30,-82,57,57,-81,-83,182,-46,192,197,-115,249,255,270,]),'TRUE':([13,14,30,35,48,49,64,65,66,],[40,40,40,40,40,40,40,40,40,]),'FALSE':([13,14,30,35,48,49,64,65,66,],[41,41,41,41,41,41,41,41,41,]),'ASSIGN':([15,16,17,71,73,119,143,197,228,241,242,270,278,282,],[43,-146,-147,97,-145,129,129,225,225,225,225,225,225,295,]),'COMMA':([15,16,17,31,58,59,60,71,73,75,76,79,80,81,82,95,101,106,115,116,117,118,119,120,140,141,142,144,170,188,189,202,203,204,205,206,207,214,219,220,221,222,223,224,226,235,244,250,251,259,260,261,262,263,264,265,266,267,290,291,292,293,294,304,310,],[44,-146,-147,-84,-79,-80,-85,44,-145,100,-15,102,-142,-143,-82,102,-81,-83,127,128,-20,-23,-21,-141,128,-19,-22,-24,-104,211,-103,228,-49,230,-75,-76,-78,230,-63,241,242,243,-62,-65,230,-102,-66,-74,-77,278,279,-61,280,-64,281,-68,-69,-70,303,281,281,-67,-71,-72,281,]),'IMPLIES':([23,25,27,31,39,58,59,60,63,82,101,106,],[-85,-80,-79,-84,69,-79,-80,-85,69,-82,-81,-83,]),'OR':([24,26,31,32,33,34,36,37,38,40,41,51,52,53,55,56,58,59,60,62,67,77,78,82,85,86,89,92,93,94,96,101,103,104,105,106,110,123,124,],[48,-122,-84,-124,-126,-129,-131,-132,-134,-139,-140,83,-87,-89,-91,-92,-79,-80,-85,48,-130,-121,-123,-82,-90,83,-133,-125,-127,-128,-136,-81,-86,-88,-93,-83,-135,-137,-138,]),'RP1':([26,31,32,33,34,36,37,38,40,41,52,53,55,56,58,59,60,62,67,74,75,76,77,78,80,81,82,85,86,87,89,92,93,94,95,96,101,103,104,105,106,108,109,110,114,115,116,117,118,119,120,121,122,123,124,140,141,142,144,197,201,202,203,213,217,219,220,221,222,223,224,244,248,259,260,261,262,263,264,265,266,267,270,272,275,283,290,291,292,293,294,304,310,],[-122,-84,-124,-126,-129,-131,-132,-134,-139,-140,-87,-89,-91,-92,-79,-80,-85,89,-130,99,-14,-15,-121,-123,-142,-143,-82,-90,105,106,-133,-125,-127,-128,110,-136,-81,-86,-88,-93,-83,123,124,-135,-13,-17,-18,-20,-23,-21,-141,-94,-95,-137,-138,-16,-19,-22,-24,218,227,-48,-49,236,238,-63,-55,-58,-60,-62,-65,-66,-47,-52,-54,-61,-57,-64,-59,-68,-69,-70,284,286,288,296,-51,-53,-56,-67,-71,-72,-50,]),'XOR':([26,31,32,33,34,36,37,38,40,41,58,59,60,67,77,78,82,89,92,93,94,96,101,106,110,123,124,],[49,-84,-124,-126,-129,-131,-132,-134,-139,-140,-79,-80,-85,-130,49,-123,-82,-133,-125,-127,-128,-136,-81,-83,-135,-137,-138,]),'AND':([31,32,33,34,36,37,38,40,41,52,53,55,56,58,59,60,67,78,82,85,89,92,93,94,96,101,103,104,105,106,110,123,124,],[-84,64,-126,-129,-131,-132,-134,-139,-140,84,-89,-91,-92,-79,-80,-85,-130,64,-82,-90,-133,-125,-127,-128,-136,-81,84,-88,-93,-83,-135,-137,-138,]),'RP3':([31,51,52,53,55,56,58,59,60,79,80,81,82,85,101,103,104,105,106,120,170,188,189,204,205,206,207,214,226,235,250,251,],[-84,82,-87,-89,-91,-92,-79,-80,-85,101,-142,-143,-82,-90,-81,-86,-88,-93,-83,-141,-104,210,-103,229,-75,-76,-78,237,245,-102,-74,-77,]),'EQ':([31,33,34,36,37,38,40,41,58,59,60,63,67,82,89,92,93,94,96,101,106,110,123,124,],[-84,65,-129,-131,-132,-134,-139,-140,-79,-80,-85,90,-130,-82,-133,65,-127,-128,-136,-81,-83,-135,-137,-138,]),'NEQ':([31,33,34,36,37,38,40,41,58,59,60,63,67,82,89,92,93,94,96,101,106,110,123,124,],[-84,66,-129,-131,-132,-134,-139,-140,-79,-80,-85,91,-130,-82,-133,66,-127,-128,-136,-81,-83,-135,-137,-138,]),'DOT':([31,58,59,60,82,88,101,106,],[-84,-79,-80,-85,-82,107,-81,-83,]),'COLON':([31,58,59,60,82,99,101,106,126,133,134,135,136,137,168,170,206,207,210,268,269,],[-84,-79,-80,-85,-82,112,-81,-83,139,148,149,150,151,152,187,-104,231,-78,234,282,-73,]),'EXTENDS':([99,],[113,]),'LP2':([112,139,148,149,150,151,152,],[125,154,156,157,158,159,160,]),'PASS':([125,154,],[132,132,]),'FN':([125,130,131,146,147,153,154,161,200,208,212,215,216,],[133,133,-26,-25,-27,-33,133,133,-28,-29,-30,-31,-32,]),'VAR':([125,130,131,146,147,153,154,161,200,208,212,215,216,],[134,134,-26,-25,-27,-33,134,134,-28,-29,-30,-31,-32,]),'CLS_FN':([125,130,131,146,147,153,154,161,200,208,212,215,216,],[135,135,-26,-25,-27,-33,135,135,-28,-29,-30,-31,-32,]),'CLS_VAR':([125,130,131,146,147,153,154,161,200,208,212,215,216,],[136,136,-26,-25,-27,-33,136,136,-28,-29,-30,-31,-32,]),'STATIC_FN':([125,130,131,146,147,153,154,161,200,208,212,215,216,],[137,137,-26,-25,-27,-33,137,137,-28,-29,-30,-31,-32,]),'error':([125,130,131,146,147,153,154,161,200,208,212,215,216,],[138,138,-26,-25,-27,-33,138,138,-28,-29,-30,-31,-32,]),'RP2':([130,131,146,147,153,161,162,163,166,167,171,172,174,175,176,181,185,186,191,196,200,208,212,215,216,232,233,239,246,253,256,273,277,285,287,289,297,299,301,305,312,313,314,315,],[145,-26,-25,-27,-33,179,180,-35,184,-97,190,-41,194,195,-106,-34,-96,-98,-40,-105,-28,-29,-30,-31,-32,-99,-100,-111,-36,-42,-107,-101,-112,-37,-43,-108,-113,-38,-44,-109,-114,-39,-45,-110,]),'STAR':([197,228,241,242,270,278,],[222,222,260,262,222,290,]),'R_ARROW':([218,227,236,238,284,286,288,296,],[240,247,254,257,298,300,302,306,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'stmts':([4,],[6,]),'stmt':([4,6,],[7,19,]),'trait_decl':([4,6,],[8,8,]),'print_stmt':([4,6,],[9,9,]),'generate_stmt':([4,6,],[10,10,]),'assign_stmt':([4,6,],[11,11,]),'names':([4,6,43,97,],[15,15,71,71,]),'name':([4,6,43,44,97,],[16,16,16,73,16,]),'trait_id':([12,],[20,]),'to_print':([13,14,],[22,42,]),'boolean_expr':([13,14,30,],[24,24,62,]),'unnamed_pred':([13,14,28,30,35,48,49,54,57,61,64,65,66,69,83,84,90,91,113,129,187,197,225,228,231,234,240,241,247,254,257,270,282,295,298,300,302,306,],[25,25,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,]),'boolean_expr_a':([13,14,30,48,],[26,26,26,77,]),'pred_name':([13,14,28,30,35,48,49,54,57,61,64,65,66,69,83,84,90,91,113,129,187,197,225,228,231,234,240,241,247,254,257,270,282,295,298,300,302,306,],[27,27,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,]),'boolean_expr_b':([13,14,30,48,49,],[32,32,32,32,78,]),'boolean_expr_c':([13,14,30,48,49,64,],[33,33,33,33,33,92,]),'boolean_expr_d':([13,14,30,48,49,64,65,66,],[34,34,34,34,34,34,93,94,]),'boolean_expr_e':([13,14,30,35,48,49,64,65,66,],[36,36,36,67,36,36,36,36,36,]),'atomic_boolean_expr':([13,14,30,35,48,49,64,65,66,],[37,37,37,37,37,37,37,37,37,]),'constants':([13,14,30,35,48,49,64,65,66,],[38,38,38,38,38,38,38,38,38,]),'unary_pred':([13,14,28,30,35,48,49,54,57,61,64,65,66,69,83,84,90,91,113,129,187,197,225,228,231,234,240,241,247,254,257,270,282,295,298,300,302,306,],[39,39,56,63,39,39,39,56,56,88,39,39,39,96,56,56,108,109,126,144,209,219,244,219,251,252,258,219,271,274,276,219,294,304,307,308,309,311,]),'pred_expr':([28,57,],[51,86,]),'pred_expr_a':([28,57,83,],[52,52,103,]),'pred_expr_b':([28,57,83,84,],[53,53,53,104,]),'pred_expr_c':([28,54,57,83,84,],[55,85,55,55,55,]),'assign_expr':([43,97,],[72,111,]),'class_args':([46,],[74,]),'main_arg':([46,],[75,]),'args':([50,68,],[79,95,]),'arg':([50,68,102,],[80,80,120,]),'var_expr':([61,],[87,]),'sub_args':([100,],[114,]),'necessary_args':([100,],[115,]),'optional_args':([100,127,],[116,140,]),'necessary_arg':([100,127,],[117,141,]),'optional_arg':([100,127,128,],[118,118,142,]),'member_var_name':([107,],[121,]),'trait_decl_stmts':([125,154,],[130,161,]),'trait_decl_stmt':([125,130,154,161,],[131,146,131,146,]),'decl_fn_stmts':([156,],[162,]),'decl_fn_stmt':([156,162,],[163,181,]),'fn_id':([156,158,162,171,],[164,173,164,173,]),'decl_stmts':([157,159,],[166,174,]),'decl_stmt':([157,159,166,174,],[167,167,185,185,]),'var_id':([157,159,166,169,174,211,],[168,168,168,189,168,235,]),'decl_cls_fn_stmts':([158,],[171,]),'decl_cls_fn_stmt':([158,171,],[172,191,]),'decl_static_fn_stmts':([160,],[175,]),'decl_static_fn_stmt':([160,175,],[176,196,]),'static_fn_id':([160,175,],[177,177,]),'vars_id':([169,],[188,]),'pred_args':([182,192,249,255,],[201,213,272,275,]),'main_pred':([182,192,249,255,],[202,202,202,202,]),'type_var_args':([183,193,198,],[204,214,226,]),'type_var_arg':([183,193,198,230,],[205,205,205,250,]),'type_var_id':([183,193,198,230,],[206,206,206,206,]),'next_preds':([197,228,270,],[217,248,283,]),'next_anonymous_necessary_preds':([197,228,270,],[220,220,220,]),'next_anonymous_opt_preds':([197,228,241,270,],[221,221,259,221,]),'next_anonymous_necessary_pred':([197,228,241,270,],[223,223,261,223,]),'next_anonymous_opt_pred':([197,228,241,242,270,278,],[224,224,224,263,224,263,]),'next_named_preds':([243,279,280,303,],[264,291,292,310,]),'next_named_pred':([243,279,280,281,303,],[265,265,265,293,265,]),'next_named_necessary_pred':([243,279,280,281,303,],[266,266,266,266,266,]),'next_named_opt_pred':([243,279,280,281,303,],[267,267,267,267,267,]),'arg_name':([243,279,280,281,303,],[268,268,268,268,268,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM_BEGIN S_COLON stmts PROGRAM_END S_COLON','program',5,'p_program_r0','parser.py',162),
  ('program -> WS','program',1,'p_program_r1','parser.py',167),
  ('stmts -> stmts stmt','stmts',2,'p_stmts_r0','parser.py',172),
  ('stmts -> stmt','stmts',1,'p_stmts_r1','parser.py',177),
  ('stmt -> trait_decl','stmt',1,'p_stmt_r0','parser.py',182),
  ('stmt -> print_stmt','stmt',1,'p_stmt_r1','parser.py',187),
  ('stmt -> generate_stmt','stmt',1,'p_stmt_r2','parser.py',192),
  ('stmt -> assign_stmt','stmt',1,'p_stmt_r3','parser.py',197),
  ('stmt -> S_COLON','stmt',1,'p_stmt_r4','parser.py',202),
  ('trait_decl -> TRAIT trait_id LP1 class_args RP1 COLON LP2 trait_decl_stmts RP2 S_COLON','trait_decl',10,'p_trait_decl_r0','parser.py',207),
  ('trait_decl -> TRAIT trait_id LP1 class_args RP1 EXTENDS unary_pred COLON LP2 trait_decl_stmts RP2 S_COLON','trait_decl',12,'p_trait_decl_r1','parser.py',212),
  ('trait_id -> ID','trait_id',1,'p_trait_id_r0','parser.py',217),
  ('class_args -> main_arg COMMA sub_args','class_args',3,'p_class_args_r0','parser.py',222),
  ('class_args -> main_arg','class_args',1,'p_class_args_r1','parser.py',227),
  ('main_arg -> ID','main_arg',1,'p_main_arg_r0','parser.py',232),
  ('sub_args -> necessary_args COMMA optional_args','sub_args',3,'p_sub_args_r0','parser.py',237),
  ('sub_args -> necessary_args','sub_args',1,'p_sub_args_r1','parser.py',242),
  ('sub_args -> optional_args','sub_args',1,'p_sub_args_r2','parser.py',247),
  ('necessary_args -> necessary_args COMMA necessary_arg','necessary_args',3,'p_necessary_args_r0','parser.py',252),
  ('necessary_args -> necessary_arg','necessary_args',1,'p_necessary_args_r1','parser.py',257),
  ('necessary_arg -> ID','necessary_arg',1,'p_necessary_arg_r0','parser.py',262),
  ('optional_args -> optional_args COMMA optional_arg','optional_args',3,'p_optional_args_r0','parser.py',267),
  ('optional_args -> optional_arg','optional_args',1,'p_optional_args_r1','parser.py',272),
  ('optional_arg -> ID ASSIGN unary_pred','optional_arg',3,'p_optional_arg_r0','parser.py',277),
  ('trait_decl_stmts -> trait_decl_stmts trait_decl_stmt','trait_decl_stmts',2,'p_trait_decl_stmts_r0','parser.py',282),
  ('trait_decl_stmts -> trait_decl_stmt','trait_decl_stmts',1,'p_trait_decl_stmts_r1','parser.py',287),
  ('trait_decl_stmts -> PASS S_COLON','trait_decl_stmts',2,'p_trait_decl_stmts_r2','parser.py',292),
  ('trait_decl_stmt -> FN COLON LP2 decl_fn_stmts RP2 S_COLON','trait_decl_stmt',6,'p_trait_decl_stmt_r0','parser.py',297),
  ('trait_decl_stmt -> VAR COLON LP2 decl_stmts RP2 S_COLON','trait_decl_stmt',6,'p_trait_decl_stmt_r1','parser.py',302),
  ('trait_decl_stmt -> CLS_FN COLON LP2 decl_cls_fn_stmts RP2 S_COLON','trait_decl_stmt',6,'p_trait_decl_stmt_r2','parser.py',307),
  ('trait_decl_stmt -> CLS_VAR COLON LP2 decl_stmts RP2 S_COLON','trait_decl_stmt',6,'p_trait_decl_stmt_r3','parser.py',312),
  ('trait_decl_stmt -> STATIC_FN COLON LP2 decl_static_fn_stmts RP2 S_COLON','trait_decl_stmt',6,'p_trait_decl_stmt_r4','parser.py',317),
  ('trait_decl_stmt -> error S_COLON','trait_decl_stmt',2,'p_trait_decl_stmt_err0','parser.py',322),
  ('decl_fn_stmts -> decl_fn_stmts decl_fn_stmt','decl_fn_stmts',2,'p_decl_fn_stmts_r0','parser.py',327),
  ('decl_fn_stmts -> decl_fn_stmt','decl_fn_stmts',1,'p_decl_fn_stmts_r1','parser.py',332),
  ('decl_fn_stmt -> fn_id LP1 pred_args RP1 S_COLON','decl_fn_stmt',5,'p_decl_fn_stmt_r0','parser.py',337),
  ('decl_fn_stmt -> fn_id LP1 pred_args RP1 R_ARROW unary_pred S_COLON','decl_fn_stmt',7,'p_decl_fn_stmt_r1','parser.py',342),
  ('decl_fn_stmt -> fn_id LP3 type_var_args RP3 LP1 pred_args RP1 S_COLON','decl_fn_stmt',8,'p_decl_fn_stmt_r2','parser.py',347),
  ('decl_fn_stmt -> fn_id LP3 type_var_args RP3 LP1 pred_args RP1 R_ARROW unary_pred S_COLON','decl_fn_stmt',10,'p_decl_fn_stmt_r3','parser.py',352),
  ('decl_cls_fn_stmts -> decl_cls_fn_stmts decl_cls_fn_stmt','decl_cls_fn_stmts',2,'p_decl_cls_fn_stmts_r0','parser.py',357),
  ('decl_cls_fn_stmts -> decl_cls_fn_stmt','decl_cls_fn_stmts',1,'p_decl_cls_fn_stmts_r1','parser.py',362),
  ('decl_cls_fn_stmt -> fn_id LP1 pred_args RP1 S_COLON','decl_cls_fn_stmt',5,'p_decl_cls_fn_stmt_r0','parser.py',367),
  ('decl_cls_fn_stmt -> fn_id LP1 pred_args RP1 R_ARROW unary_pred S_COLON','decl_cls_fn_stmt',7,'p_decl_cls_fn_stmt_r1','parser.py',372),
  ('decl_cls_fn_stmt -> fn_id LP3 type_var_args RP3 LP1 pred_args RP1 S_COLON','decl_cls_fn_stmt',8,'p_decl_cls_fn_stmt_r2','parser.py',377),
  ('decl_cls_fn_stmt -> fn_id LP3 type_var_args RP3 LP1 pred_args RP1 R_ARROW unary_pred S_COLON','decl_cls_fn_stmt',10,'p_decl_cls_fn_stmt_r3','parser.py',382),
  ('fn_id -> ID','fn_id',1,'p_fn_id_r0','parser.py',387),
  ('pred_args -> main_pred COMMA next_preds','pred_args',3,'p_pred_args_r0','parser.py',392),
  ('pred_args -> main_pred','pred_args',1,'p_pred_args_r1','parser.py',397),
  ('main_pred -> ID','main_pred',1,'p_main_pred_r0','parser.py',402),
  ('next_preds -> next_anonymous_necessary_preds COMMA next_anonymous_opt_preds COMMA STAR COMMA next_named_preds','next_preds',7,'p_next_preds_r0','parser.py',407),
  ('next_preds -> next_anonymous_necessary_preds COMMA next_anonymous_opt_preds COMMA STAR','next_preds',5,'p_next_preds_r1','parser.py',412),
  ('next_preds -> next_anonymous_necessary_preds COMMA next_anonymous_opt_preds','next_preds',3,'p_next_preds_r2','parser.py',417),
  ('next_preds -> next_anonymous_necessary_preds COMMA STAR COMMA next_named_preds','next_preds',5,'p_next_preds_r3','parser.py',422),
  ('next_preds -> next_anonymous_necessary_preds COMMA STAR','next_preds',3,'p_next_preds_r4','parser.py',427),
  ('next_preds -> next_anonymous_necessary_preds','next_preds',1,'p_next_preds_r5','parser.py',432),
  ('next_preds -> next_anonymous_opt_preds COMMA STAR COMMA next_named_preds','next_preds',5,'p_next_preds_r6','parser.py',437),
  ('next_preds -> next_anonymous_opt_preds COMMA STAR','next_preds',3,'p_next_preds_r7','parser.py',442),
  ('next_preds -> next_anonymous_opt_preds','next_preds',1,'p_next_preds_r8','parser.py',447),
  ('next_preds -> STAR COMMA next_named_preds','next_preds',3,'p_next_preds_r9','parser.py',452),
  ('next_preds -> STAR','next_preds',1,'p_next_preds_r10','parser.py',457),
  ('next_anonymous_necessary_preds -> next_anonymous_necessary_preds COMMA next_anonymous_necessary_pred','next_anonymous_necessary_preds',3,'p_next_anonymous_necessary_preds_r0','parser.py',462),
  ('next_anonymous_necessary_preds -> next_anonymous_necessary_pred','next_anonymous_necessary_preds',1,'p_next_anonymous_necessary_preds_r1','parser.py',467),
  ('next_anonymous_necessary_pred -> unary_pred','next_anonymous_necessary_pred',1,'p_next_anonymous_necessary_pred_r0','parser.py',472),
  ('next_anonymous_opt_preds -> next_anonymous_opt_preds COMMA next_anonymous_opt_pred','next_anonymous_opt_preds',3,'p_next_anonymous_opt_preds_r0','parser.py',477),
  ('next_anonymous_opt_preds -> next_anonymous_opt_pred','next_anonymous_opt_preds',1,'p_next_anonymous_opt_preds_r1','parser.py',482),
  ('next_anonymous_opt_pred -> ASSIGN unary_pred','next_anonymous_opt_pred',2,'p_next_anonymous_opt_pred_r0','parser.py',487),
  ('next_named_preds -> next_named_preds COMMA next_named_pred','next_named_preds',3,'p_next_named_preds_r0','parser.py',492),
  ('next_named_preds -> next_named_pred','next_named_preds',1,'p_next_named_preds_r1','parser.py',497),
  ('next_named_pred -> next_named_necessary_pred','next_named_pred',1,'p_next_named_pred_r0','parser.py',502),
  ('next_named_pred -> next_named_opt_pred','next_named_pred',1,'p_next_named_pred_r1','parser.py',507),
  ('next_named_necessary_pred -> arg_name COLON unary_pred','next_named_necessary_pred',3,'p_next_named_necessary_pred_r0','parser.py',512),
  ('next_named_opt_pred -> arg_name COLON ASSIGN unary_pred','next_named_opt_pred',4,'p_next_named_opt_pred_r0','parser.py',517),
  ('arg_name -> ID','arg_name',1,'p_arg_name_r0','parser.py',522),
  ('type_var_args -> type_var_args COMMA type_var_arg','type_var_args',3,'p_type_var_args_r0','parser.py',527),
  ('type_var_args -> type_var_arg','type_var_args',1,'p_type_var_args_r1','parser.py',532),
  ('type_var_arg -> type_var_id','type_var_arg',1,'p_type_var_arg_r0','parser.py',537),
  ('type_var_arg -> type_var_id COLON unary_pred','type_var_arg',3,'p_type_var_arg_r1','parser.py',542),
  ('type_var_id -> ID','type_var_id',1,'p_type_var_id_r0','parser.py',547),
  ('unary_pred -> pred_name','unary_pred',1,'p_unary_pred_r0','parser.py',552),
  ('unary_pred -> unnamed_pred','unary_pred',1,'p_unary_pred_r1','parser.py',557),
  ('unnamed_pred -> pred_name LP3 args RP3','unnamed_pred',4,'p_unnamed_pred_r0','parser.py',562),
  ('unnamed_pred -> LP3 pred_expr RP3','unnamed_pred',3,'p_unnamed_pred_r1','parser.py',567),
  ('unnamed_pred -> TRAIT_OF LP1 var_expr RP1','unnamed_pred',4,'p_unnamed_pred_r2','parser.py',572),
  ('unnamed_pred -> NONE','unnamed_pred',1,'p_unnamed_pred_r3','parser.py',577),
  ('pred_name -> ID','pred_name',1,'p_pred_name_r0','parser.py',582),
  ('pred_expr -> pred_expr OR pred_expr_a','pred_expr',3,'p_pred_expr_r0','parser.py',587),
  ('pred_expr -> pred_expr_a','pred_expr',1,'p_pred_expr_r1','parser.py',592),
  ('pred_expr_a -> pred_expr_a AND pred_expr_b','pred_expr_a',3,'p_pred_expr_a_r0','parser.py',597),
  ('pred_expr_a -> pred_expr_b','pred_expr_a',1,'p_pred_expr_a_r1','parser.py',602),
  ('pred_expr_b -> NOT pred_expr_c','pred_expr_b',2,'p_pred_expr_b_r0','parser.py',607),
  ('pred_expr_b -> pred_expr_c','pred_expr_b',1,'p_pred_expr_b_r1','parser.py',612),
  ('pred_expr_c -> unary_pred','pred_expr_c',1,'p_pred_expr_c_r0','parser.py',617),
  ('pred_expr_c -> LP1 pred_expr RP1','pred_expr_c',3,'p_pred_expr_c_r1','parser.py',622),
  ('var_expr -> unary_pred DOT member_var_name','var_expr',3,'p_var_expr_r0','parser.py',627),
  ('member_var_name -> ID','member_var_name',1,'p_member_var_name_r0','parser.py',632),
  ('decl_stmts -> decl_stmts decl_stmt','decl_stmts',2,'p_decl_stmts_r0','parser.py',637),
  ('decl_stmts -> decl_stmt','decl_stmts',1,'p_decl_stmts_r1','parser.py',642),
  ('decl_stmt -> var_id S_COLON','decl_stmt',2,'p_decl_stmt_r0','parser.py',647),
  ('decl_stmt -> var_id COLON unary_pred S_COLON','decl_stmt',4,'p_decl_stmt_r1','parser.py',652),
  ('decl_stmt -> LP3 vars_id RP3 S_COLON','decl_stmt',4,'p_decl_stmt_r2','parser.py',657),
  ('decl_stmt -> LP3 vars_id RP3 COLON unary_pred S_COLON','decl_stmt',6,'p_decl_stmt_r3','parser.py',662),
  ('vars_id -> vars_id COMMA var_id','vars_id',3,'p_vars_id_r0','parser.py',667),
  ('vars_id -> var_id','vars_id',1,'p_vars_id_r1','parser.py',672),
  ('var_id -> ID','var_id',1,'p_var_id_r0','parser.py',677),
  ('decl_static_fn_stmts -> decl_static_fn_stmts decl_static_fn_stmt','decl_static_fn_stmts',2,'p_decl_static_fn_stmts_r0','parser.py',682),
  ('decl_static_fn_stmts -> decl_static_fn_stmt','decl_static_fn_stmts',1,'p_decl_static_fn_stmts_r1','parser.py',687),
  ('decl_static_fn_stmt -> static_fn_id LP1 next_preds RP1 S_COLON','decl_static_fn_stmt',5,'p_decl_static_fn_stmt_r0','parser.py',692),
  ('decl_static_fn_stmt -> static_fn_id LP1 next_preds RP1 R_ARROW unary_pred S_COLON','decl_static_fn_stmt',7,'p_decl_static_fn_stmt_r1','parser.py',697),
  ('decl_static_fn_stmt -> static_fn_id LP3 type_var_args RP3 LP1 next_preds RP1 S_COLON','decl_static_fn_stmt',8,'p_decl_static_fn_stmt_r2','parser.py',702),
  ('decl_static_fn_stmt -> static_fn_id LP3 type_var_args RP3 LP1 next_preds RP1 R_ARROW unary_pred S_COLON','decl_static_fn_stmt',10,'p_decl_static_fn_stmt_r3','parser.py',707),
  ('decl_static_fn_stmt -> static_fn_id LP1 RP1 S_COLON','decl_static_fn_stmt',4,'p_decl_static_fn_stmt_r4','parser.py',712),
  ('decl_static_fn_stmt -> static_fn_id LP1 RP1 R_ARROW unary_pred S_COLON','decl_static_fn_stmt',6,'p_decl_static_fn_stmt_r5','parser.py',717),
  ('decl_static_fn_stmt -> static_fn_id LP3 type_var_args RP3 LP1 RP1 S_COLON','decl_static_fn_stmt',7,'p_decl_static_fn_stmt_r6','parser.py',722),
  ('decl_static_fn_stmt -> static_fn_id LP3 type_var_args RP3 LP1 RP1 R_ARROW unary_pred S_COLON','decl_static_fn_stmt',9,'p_decl_static_fn_stmt_r7','parser.py',727),
  ('static_fn_id -> ID','static_fn_id',1,'p_static_fn_id_r0','parser.py',732),
  ('print_stmt -> PRINTINFO to_print S_COLON','print_stmt',3,'p_print_stmt_r0','parser.py',737),
  ('generate_stmt -> GENERATE to_print S_COLON','generate_stmt',3,'p_generate_stmt_r0','parser.py',742),
  ('to_print -> ID','to_print',1,'p_to_print_r0','parser.py',747),
  ('to_print -> boolean_expr','to_print',1,'p_to_print_r1','parser.py',752),
  ('to_print -> unnamed_pred','to_print',1,'p_to_print_r2','parser.py',757),
  ('boolean_expr -> boolean_expr OR boolean_expr_a','boolean_expr',3,'p_boolean_expr_r0','parser.py',762),
  ('boolean_expr -> boolean_expr_a','boolean_expr',1,'p_boolean_expr_r1','parser.py',767),
  ('boolean_expr_a -> boolean_expr_a XOR boolean_expr_b','boolean_expr_a',3,'p_boolean_expr_a_r0','parser.py',772),
  ('boolean_expr_a -> boolean_expr_b','boolean_expr_a',1,'p_boolean_expr_a_r1','parser.py',777),
  ('boolean_expr_b -> boolean_expr_b AND boolean_expr_c','boolean_expr_b',3,'p_boolean_expr_b_r0','parser.py',782),
  ('boolean_expr_b -> boolean_expr_c','boolean_expr_b',1,'p_boolean_expr_b_r1','parser.py',787),
  ('boolean_expr_c -> boolean_expr_c EQ boolean_expr_d','boolean_expr_c',3,'p_boolean_expr_c_r0','parser.py',792),
  ('boolean_expr_c -> boolean_expr_c NEQ boolean_expr_d','boolean_expr_c',3,'p_boolean_expr_c_r1','parser.py',797),
  ('boolean_expr_c -> boolean_expr_d','boolean_expr_c',1,'p_boolean_expr_c_r2','parser.py',802),
  ('boolean_expr_d -> NOT boolean_expr_e','boolean_expr_d',2,'p_boolean_expr_d_r0','parser.py',807),
  ('boolean_expr_d -> boolean_expr_e','boolean_expr_d',1,'p_boolean_expr_d_r1','parser.py',812),
  ('boolean_expr_e -> atomic_boolean_expr','boolean_expr_e',1,'p_boolean_expr_e_r0','parser.py',817),
  ('boolean_expr_e -> LP1 boolean_expr RP1','boolean_expr_e',3,'p_boolean_expr_e_r1','parser.py',822),
  ('atomic_boolean_expr -> constants','atomic_boolean_expr',1,'p_atomic_boolean_expr_r0','parser.py',827),
  ('atomic_boolean_expr -> unary_pred LP1 args RP1','atomic_boolean_expr',4,'p_atomic_boolean_expr_r1','parser.py',832),
  ('atomic_boolean_expr -> unary_pred IMPLIES unary_pred','atomic_boolean_expr',3,'p_atomic_boolean_expr_r2','parser.py',837),
  ('atomic_boolean_expr -> LP1 unary_pred EQ unary_pred RP1','atomic_boolean_expr',5,'p_atomic_boolean_expr_r3','parser.py',842),
  ('atomic_boolean_expr -> LP1 unary_pred NEQ unary_pred RP1','atomic_boolean_expr',5,'p_atomic_boolean_expr_r4','parser.py',847),
  ('constants -> TRUE','constants',1,'p_constants_r0','parser.py',852),
  ('constants -> FALSE','constants',1,'p_constants_r1','parser.py',857),
  ('args -> args COMMA arg','args',3,'p_args_r0','parser.py',862),
  ('args -> arg','args',1,'p_args_r1','parser.py',867),
  ('arg -> ID','arg',1,'p_arg_r0','parser.py',872),
  ('assign_stmt -> names ASSIGN assign_expr S_COLON','assign_stmt',4,'p_assign_stmt_r0','parser.py',877),
  ('names -> names COMMA name','names',3,'p_names_r0','parser.py',882),
  ('names -> name','names',1,'p_names_r1','parser.py',887),
  ('name -> ID','name',1,'p_name_r0','parser.py',892),
  ('assign_expr -> names ASSIGN assign_expr','assign_expr',3,'p_assign_expr_r0','parser.py',897),
  ('assign_expr -> names','assign_expr',1,'p_assign_expr_r1','parser.py',902),
]
