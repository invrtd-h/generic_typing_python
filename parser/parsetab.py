
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASSIGN CLS_FN CLS_VAR COLON COMMA DOT EQ EXTENDS FALSE FN GENERATE ID IMPLIES LP1 LP2 LP3 NEQ NONE NOT OR PASS PRINTINFO PROGRAM_BEGIN PROGRAM_END RP1 RP2 RP3 R_ARROW STAR STATIC_FN S_COLON TRAIT TRAIT_OF TRUE VAR WS XOR program : PROGRAM_BEGIN S_COLON stmts PROGRAM_END S_COLON  program : WS  stmts : stmts stmt  stmts : stmt  stmt : trait_decl  stmt : print_stmt  stmt : generate_stmt  stmt : assign_stmt  stmt : S_COLON  trait_decl : TRAIT trait_id LP1 class_args RP1 COLON LP2 trait_decl_stmts RP2 S_COLON  trait_decl : TRAIT trait_id LP1 class_args RP1 EXTENDS unary_pred COLON LP2 trait_decl_stmts RP2 S_COLON  trait_id : ID  class_args : main_arg COMMA sub_args  class_args : main_arg  main_arg : ID  sub_args : necessary_args COMMA optional_args sub_args : necessary_args  sub_args : optional_args  necessary_args : necessary_args COMMA necessary_arg  necessary_args : necessary_arg  necessary_arg : ID  optional_args : optional_args COMMA optional_arg  optional_args : optional_arg  optional_arg : ID ASSIGN unary_pred trait_decl_stmts : trait_decl_stmts trait_decl_stmt  trait_decl_stmts : trait_decl_stmt  trait_decl_stmts : PASS S_COLON  trait_decl_stmt : FN COLON LP2 decl_fn_stmts RP2 S_COLON  trait_decl_stmt : VAR COLON LP2 decl_stmts RP2 S_COLON  trait_decl_stmt : CLS_FN COLON LP2 decl_cls_fn_stmts RP2 S_COLON  trait_decl_stmt : CLS_VAR COLON LP2 decl_stmts RP2 S_COLON  trait_decl_stmt : STATIC_FN COLON LP2 decl_static_fn_stmts RP2 S_COLON  decl_fn_stmts : decl_fn_stmts decl_fn_stmt  decl_fn_stmts : decl_fn_stmt  decl_fn_stmt : fn_id LP1 pred_args RP1 S_COLON  decl_fn_stmt : fn_id LP1 pred_args RP1 R_ARROW unary_pred S_COLON  decl_fn_stmt : fn_id LP3 type_var_args RP3 LP1 pred_args RP1 S_COLON  decl_fn_stmt : fn_id LP3 type_var_args RP3 LP1 pred_args RP1 R_ARROW unary_pred S_COLON  decl_cls_fn_stmts : decl_cls_fn_stmts decl_cls_fn_stmt  decl_cls_fn_stmts : decl_cls_fn_stmt  decl_cls_fn_stmt : fn_id LP1 pred_args RP1 S_COLON  decl_cls_fn_stmt : fn_id LP1 pred_args RP1 R_ARROW unary_pred S_COLON  decl_cls_fn_stmt : fn_id LP3 type_var_args RP3 LP1 pred_args RP1 S_COLON  decl_cls_fn_stmt : fn_id LP3 type_var_args RP3 LP1 pred_args RP1 R_ARROW unary_pred S_COLON  fn_id : ID  pred_args : main_pred COMMA next_preds  pred_args : main_pred  main_pred : ID  next_preds : next_anonymous_necessary_preds COMMA next_anonymous_opt_preds COMMA STAR COMMA next_named_preds  next_preds : next_anonymous_necessary_preds COMMA next_anonymous_opt_preds COMMA STAR  next_preds : next_anonymous_necessary_preds COMMA next_anonymous_opt_preds next_preds : next_anonymous_necessary_preds COMMA STAR COMMA next_named_preds  next_preds : next_anonymous_necessary_preds COMMA STAR  next_preds : next_anonymous_necessary_preds  next_preds : next_anonymous_opt_preds COMMA STAR COMMA next_named_preds  next_preds : next_anonymous_opt_preds COMMA STAR  next_preds : next_anonymous_opt_preds  next_preds : STAR COMMA next_named_preds  next_preds : STAR  next_anonymous_necessary_preds : next_anonymous_necessary_preds COMMA next_anonymous_necessary_pred  next_anonymous_necessary_preds : next_anonymous_necessary_pred  next_anonymous_necessary_pred : unary_pred  next_anonymous_opt_preds : next_anonymous_opt_preds COMMA next_anonymous_opt_pred  next_anonymous_opt_preds : next_anonymous_opt_pred  next_anonymous_opt_pred : ASSIGN unary_pred  next_named_preds : next_named_preds COMMA next_named_pred  next_named_preds : next_named_pred  next_named_pred : next_named_necessary_pred  next_named_pred : next_named_opt_pred  next_named_necessary_pred : arg_name COLON unary_pred  next_named_opt_pred : arg_name COLON ASSIGN unary_pred  arg_name : ID  type_var_args : type_var_args COMMA type_var_arg  type_var_args : type_var_arg  type_var_arg : type_var_id  type_var_arg : type_var_id COLON unary_pred  type_var_id : ID  unary_pred : pred_name  unary_pred : unnamed_pred  unnamed_pred : pred_name LP3 args RP3  unnamed_pred : LP3 pred_expr RP3  unnamed_pred : TRAIT_OF LP1 var_expr RP1  unnamed_pred : NONE  pred_name : ID  pred_expr : pred_expr OR pred_expr_a  pred_expr : pred_expr_a  pred_expr_a : pred_expr_a AND pred_expr_b  pred_expr_a : pred_expr_b  pred_expr_b : NOT pred_expr_c  pred_expr_b : pred_expr_c  pred_expr_c : unary_pred  pred_expr_c : LP1 pred_expr RP1  var_expr : unary_pred DOT member_var_name  member_var_name : ID  decl_stmts : decl_stmts decl_stmt  decl_stmts : decl_stmt  decl_stmt : var_id S_COLON  decl_stmt : var_id COLON unary_pred S_COLON  decl_stmt : LP3 vars_id RP3 S_COLON  decl_stmt : LP3 vars_id RP3 COLON unary_pred S_COLON  vars_id : vars_id COMMA var_id  vars_id : var_id  var_id : ID  decl_static_fn_stmts : decl_static_fn_stmts decl_static_fn_stmt  decl_static_fn_stmts : decl_static_fn_stmt  decl_static_fn_stmt : static_fn_id LP1 next_preds RP1 S_COLON  decl_static_fn_stmt : static_fn_id LP1 next_preds RP1 R_ARROW unary_pred S_COLON  decl_static_fn_stmt : static_fn_id LP3 type_var_args RP3 LP1 next_preds RP1 S_COLON  decl_static_fn_stmt : static_fn_id LP3 type_var_args RP3 LP1 next_preds RP1 R_ARROW unary_pred S_COLON  decl_static_fn_stmt : static_fn_id LP1 RP1 S_COLON  decl_static_fn_stmt : static_fn_id LP1 RP1 R_ARROW unary_pred S_COLON  decl_static_fn_stmt : static_fn_id LP3 type_var_args RP3 LP1 RP1 S_COLON  decl_static_fn_stmt : static_fn_id LP3 type_var_args RP3 LP1 RP1 R_ARROW unary_pred S_COLON  static_fn_id : ID  print_stmt : PRINTINFO to_print S_COLON  generate_stmt : GENERATE to_print S_COLON  to_print : ID  to_print : boolean_expr  to_print : unnamed_pred  boolean_expr : boolean_expr OR boolean_expr_a  boolean_expr : boolean_expr_a  boolean_expr_a : boolean_expr_a XOR boolean_expr_b  boolean_expr_a : boolean_expr_b  boolean_expr_b : boolean_expr_b AND boolean_expr_c  boolean_expr_b : boolean_expr_c  boolean_expr_c : boolean_expr_c EQ boolean_expr_d  boolean_expr_c : boolean_expr_c NEQ boolean_expr_d  boolean_expr_c : boolean_expr_d  boolean_expr_d : NOT boolean_expr_e  boolean_expr_d : boolean_expr_e  boolean_expr_e : atomic_boolean_expr  boolean_expr_e : LP1 boolean_expr RP1  atomic_boolean_expr : constants  atomic_boolean_expr : unary_pred LP1 args RP1  atomic_boolean_expr : unary_pred IMPLIES unary_pred  atomic_boolean_expr : LP1 unary_pred EQ unary_pred RP1  atomic_boolean_expr : LP1 unary_pred NEQ unary_pred RP1  constants : TRUE  constants : FALSE  args : args COMMA arg  args : arg  arg : ID  assign_stmt : names ASSIGN assign_expr S_COLON  names : names COMMA name  names : name  name : ID  assign_expr : names ASSIGN assign_expr  assign_expr : names '
    
_lr_action_items = {'PROGRAM_BEGIN':([0,],[2,]),'WS':([0,],[3,]),'$end':([1,3,45,],[0,-2,-1,]),'S_COLON':([2,4,5,6,7,8,9,10,11,16,17,18,19,22,23,24,25,26,31,32,33,34,36,37,38,40,41,42,47,58,59,60,67,70,71,72,73,77,78,82,89,92,93,94,96,98,101,106,110,111,123,124,132,144,153,166,168,177,178,182,188,192,193,197,207,208,216,225,234,236,250,256,269,272,274,282,284,286,294,305,306,307,309,],[4,5,-9,5,-4,-5,-6,-7,-8,-145,-146,45,-3,47,-117,-118,-119,-121,-83,-123,-125,-128,-130,-131,-133,-138,-139,70,-115,-78,-79,-84,-129,-116,-148,98,-144,-120,-122,-81,-132,-124,-126,-127,-135,-143,-80,-82,-134,-147,-136,-137,146,153,-10,184,-103,197,198,206,210,213,214,-11,230,231,237,244,251,254,271,275,283,285,287,295,297,299,303,310,311,312,313,]),'TRAIT':([4,5,6,7,8,9,10,11,19,47,70,98,153,197,],[12,-9,12,-4,-5,-6,-7,-8,-3,-115,-116,-143,-10,-11,]),'PRINTINFO':([4,5,6,7,8,9,10,11,19,47,70,98,153,197,],[13,-9,13,-4,-5,-6,-7,-8,-3,-115,-116,-143,-10,-11,]),'GENERATE':([4,5,6,7,8,9,10,11,19,47,70,98,153,197,],[14,-9,14,-4,-5,-6,-7,-8,-3,-115,-116,-143,-10,-11,]),'ID':([4,5,6,7,8,9,10,11,12,13,14,19,28,30,35,43,44,46,47,48,49,50,54,57,61,64,65,66,68,69,70,83,84,90,91,97,98,100,102,107,113,127,128,129,153,154,155,156,157,158,160,161,164,165,167,169,170,172,173,174,179,180,181,183,184,185,189,190,191,194,195,196,197,209,223,226,228,229,230,231,232,237,238,239,241,244,245,247,251,252,253,254,255,268,271,275,277,278,279,280,283,285,287,293,295,296,297,298,299,300,301,303,304,310,311,312,313,],[17,-9,17,-4,-5,-6,-7,-8,21,23,23,-3,60,60,60,17,17,76,-115,60,60,81,60,60,60,60,60,60,81,60,-116,60,60,60,60,17,-143,119,81,122,60,119,142,60,-10,163,168,163,168,176,163,-34,168,-96,168,163,-40,168,176,-105,-33,201,205,-95,-97,60,-39,201,205,-104,60,205,-11,168,60,60,205,60,-98,-99,60,-110,60,60,267,-35,60,201,-41,60,201,-106,60,60,-100,-111,267,267,267,60,-36,-42,-107,60,-112,60,-37,60,-43,60,267,-108,60,-113,-38,-44,-109,]),'PROGRAM_END':([5,6,7,8,9,10,11,19,47,70,98,153,197,],[-9,18,-4,-5,-6,-7,-8,-3,-115,-116,-143,-10,-11,]),'LP3':([13,14,23,27,28,30,35,48,49,54,57,58,60,61,64,65,66,69,83,84,90,91,113,129,155,157,162,163,164,165,171,172,175,176,183,184,185,195,223,226,229,230,231,232,238,239,245,252,255,268,271,280,293,296,298,300,304,],[28,28,-84,50,28,28,28,28,28,28,28,50,-84,28,28,28,28,28,28,28,28,28,28,28,167,167,181,-45,167,-96,191,167,196,-114,-95,-97,28,28,28,28,28,-98,-99,28,28,28,28,28,28,28,-100,28,28,28,28,28,28,]),'TRAIT_OF':([13,14,28,30,35,48,49,54,57,61,64,65,66,69,83,84,90,91,113,129,185,195,223,226,229,232,238,239,245,252,255,268,280,293,296,298,300,304,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'NONE':([13,14,28,30,35,48,49,54,57,61,64,65,66,69,83,84,90,91,113,129,185,195,223,226,229,232,238,239,245,252,255,268,280,293,296,298,300,304,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'NOT':([13,14,28,30,48,49,57,64,65,66,83,84,],[35,35,54,35,35,35,54,35,35,35,54,54,]),'LP1':([13,14,20,21,23,25,27,28,29,30,31,35,39,48,49,54,57,58,59,60,63,64,65,66,82,83,84,101,106,162,163,171,175,176,227,235,243,],[30,30,46,-12,-84,-79,-78,57,61,30,-83,30,68,30,30,57,57,-78,-79,-84,68,30,30,30,-81,57,57,-80,-82,180,-45,190,195,-114,247,253,268,]),'TRUE':([13,14,30,35,48,49,64,65,66,],[40,40,40,40,40,40,40,40,40,]),'FALSE':([13,14,30,35,48,49,64,65,66,],[41,41,41,41,41,41,41,41,41,]),'ASSIGN':([15,16,17,71,73,119,142,195,226,239,240,268,276,280,],[43,-145,-146,97,-144,129,129,223,223,223,223,223,223,293,]),'COMMA':([15,16,17,31,58,59,60,71,73,75,76,79,80,81,82,95,101,106,115,116,117,118,119,120,139,140,141,143,168,186,187,200,201,202,203,204,205,212,217,218,219,220,221,222,224,233,242,248,249,257,258,259,260,261,262,263,264,265,288,289,290,291,292,302,308,],[44,-145,-146,-83,-78,-79,-84,44,-144,100,-15,102,-141,-142,-81,102,-80,-82,127,128,-20,-23,-21,-140,128,-19,-22,-24,-103,209,-102,226,-48,228,-74,-75,-77,228,-62,239,240,241,-61,-64,228,-101,-65,-73,-76,276,277,-60,278,-63,279,-67,-68,-69,301,279,279,-66,-70,-71,279,]),'IMPLIES':([23,25,27,31,39,58,59,60,63,82,101,106,],[-84,-79,-78,-83,69,-78,-79,-84,69,-81,-80,-82,]),'OR':([24,26,31,32,33,34,36,37,38,40,41,51,52,53,55,56,58,59,60,62,67,77,78,82,85,86,89,92,93,94,96,101,103,104,105,106,110,123,124,],[48,-121,-83,-123,-125,-128,-130,-131,-133,-138,-139,83,-86,-88,-90,-91,-78,-79,-84,48,-129,-120,-122,-81,-89,83,-132,-124,-126,-127,-135,-80,-85,-87,-92,-82,-134,-136,-137,]),'RP1':([26,31,32,33,34,36,37,38,40,41,52,53,55,56,58,59,60,62,67,74,75,76,77,78,80,81,82,85,86,87,89,92,93,94,95,96,101,103,104,105,106,108,109,110,114,115,116,117,118,119,120,121,122,123,124,139,140,141,143,195,199,200,201,211,215,217,218,219,220,221,222,242,246,257,258,259,260,261,262,263,264,265,268,270,273,281,288,289,290,291,292,302,308,],[-121,-83,-123,-125,-128,-130,-131,-133,-138,-139,-86,-88,-90,-91,-78,-79,-84,89,-129,99,-14,-15,-120,-122,-141,-142,-81,-89,105,106,-132,-124,-126,-127,110,-135,-80,-85,-87,-92,-82,123,124,-134,-13,-17,-18,-20,-23,-21,-140,-93,-94,-136,-137,-16,-19,-22,-24,216,225,-47,-48,234,236,-62,-54,-57,-59,-61,-64,-65,-46,-51,-53,-60,-56,-63,-58,-67,-68,-69,282,284,286,294,-50,-52,-55,-66,-70,-71,-49,]),'XOR':([26,31,32,33,34,36,37,38,40,41,58,59,60,67,77,78,82,89,92,93,94,96,101,106,110,123,124,],[49,-83,-123,-125,-128,-130,-131,-133,-138,-139,-78,-79,-84,-129,49,-122,-81,-132,-124,-126,-127,-135,-80,-82,-134,-136,-137,]),'AND':([31,32,33,34,36,37,38,40,41,52,53,55,56,58,59,60,67,78,82,85,89,92,93,94,96,101,103,104,105,106,110,123,124,],[-83,64,-125,-128,-130,-131,-133,-138,-139,84,-88,-90,-91,-78,-79,-84,-129,64,-81,-89,-132,-124,-126,-127,-135,-80,84,-87,-92,-82,-134,-136,-137,]),'RP3':([31,51,52,53,55,56,58,59,60,79,80,81,82,85,101,103,104,105,106,120,168,186,187,202,203,204,205,212,224,233,248,249,],[-83,82,-86,-88,-90,-91,-78,-79,-84,101,-141,-142,-81,-89,-80,-85,-87,-92,-82,-140,-103,208,-102,227,-74,-75,-77,235,243,-101,-73,-76,]),'EQ':([31,33,34,36,37,38,40,41,58,59,60,63,67,82,89,92,93,94,96,101,106,110,123,124,],[-83,65,-128,-130,-131,-133,-138,-139,-78,-79,-84,90,-129,-81,-132,65,-126,-127,-135,-80,-82,-134,-136,-137,]),'NEQ':([31,33,34,36,37,38,40,41,58,59,60,63,67,82,89,92,93,94,96,101,106,110,123,124,],[-83,66,-128,-130,-131,-133,-138,-139,-78,-79,-84,91,-129,-81,-132,66,-126,-127,-135,-80,-82,-134,-136,-137,]),'DOT':([31,58,59,60,82,88,101,106,],[-83,-78,-79,-84,-81,107,-80,-82,]),'COLON':([31,58,59,60,82,99,101,106,126,133,134,135,136,137,166,168,204,205,208,266,267,],[-83,-78,-79,-84,-81,112,-80,-82,138,147,148,149,150,151,185,-103,229,-77,232,280,-72,]),'EXTENDS':([99,],[113,]),'LP2':([112,138,147,148,149,150,151,],[125,152,154,155,156,157,158,]),'PASS':([125,152,],[132,132,]),'FN':([125,130,131,145,146,152,159,198,206,210,213,214,],[133,133,-26,-25,-27,133,133,-28,-29,-30,-31,-32,]),'VAR':([125,130,131,145,146,152,159,198,206,210,213,214,],[134,134,-26,-25,-27,134,134,-28,-29,-30,-31,-32,]),'CLS_FN':([125,130,131,145,146,152,159,198,206,210,213,214,],[135,135,-26,-25,-27,135,135,-28,-29,-30,-31,-32,]),'CLS_VAR':([125,130,131,145,146,152,159,198,206,210,213,214,],[136,136,-26,-25,-27,136,136,-28,-29,-30,-31,-32,]),'STATIC_FN':([125,130,131,145,146,152,159,198,206,210,213,214,],[137,137,-26,-25,-27,137,137,-28,-29,-30,-31,-32,]),'RP2':([130,131,145,146,159,160,161,164,165,169,170,172,173,174,179,183,184,189,194,198,206,210,213,214,230,231,237,244,251,254,271,275,283,285,287,295,297,299,303,310,311,312,313,],[144,-26,-25,-27,177,178,-34,182,-96,188,-40,192,193,-105,-33,-95,-97,-39,-104,-28,-29,-30,-31,-32,-98,-99,-110,-35,-41,-106,-100,-111,-36,-42,-107,-112,-37,-43,-108,-113,-38,-44,-109,]),'STAR':([195,226,239,240,268,276,],[220,220,258,260,220,288,]),'R_ARROW':([216,225,234,236,282,284,286,294,],[238,245,252,255,296,298,300,304,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'stmts':([4,],[6,]),'stmt':([4,6,],[7,19,]),'trait_decl':([4,6,],[8,8,]),'print_stmt':([4,6,],[9,9,]),'generate_stmt':([4,6,],[10,10,]),'assign_stmt':([4,6,],[11,11,]),'names':([4,6,43,97,],[15,15,71,71,]),'name':([4,6,43,44,97,],[16,16,16,73,16,]),'trait_id':([12,],[20,]),'to_print':([13,14,],[22,42,]),'boolean_expr':([13,14,30,],[24,24,62,]),'unnamed_pred':([13,14,28,30,35,48,49,54,57,61,64,65,66,69,83,84,90,91,113,129,185,195,223,226,229,232,238,239,245,252,255,268,280,293,296,298,300,304,],[25,25,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,]),'boolean_expr_a':([13,14,30,48,],[26,26,26,77,]),'pred_name':([13,14,28,30,35,48,49,54,57,61,64,65,66,69,83,84,90,91,113,129,185,195,223,226,229,232,238,239,245,252,255,268,280,293,296,298,300,304,],[27,27,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,]),'boolean_expr_b':([13,14,30,48,49,],[32,32,32,32,78,]),'boolean_expr_c':([13,14,30,48,49,64,],[33,33,33,33,33,92,]),'boolean_expr_d':([13,14,30,48,49,64,65,66,],[34,34,34,34,34,34,93,94,]),'boolean_expr_e':([13,14,30,35,48,49,64,65,66,],[36,36,36,67,36,36,36,36,36,]),'atomic_boolean_expr':([13,14,30,35,48,49,64,65,66,],[37,37,37,37,37,37,37,37,37,]),'constants':([13,14,30,35,48,49,64,65,66,],[38,38,38,38,38,38,38,38,38,]),'unary_pred':([13,14,28,30,35,48,49,54,57,61,64,65,66,69,83,84,90,91,113,129,185,195,223,226,229,232,238,239,245,252,255,268,280,293,296,298,300,304,],[39,39,56,63,39,39,39,56,56,88,39,39,39,96,56,56,108,109,126,143,207,217,242,217,249,250,256,217,269,272,274,217,292,302,305,306,307,309,]),'pred_expr':([28,57,],[51,86,]),'pred_expr_a':([28,57,83,],[52,52,103,]),'pred_expr_b':([28,57,83,84,],[53,53,53,104,]),'pred_expr_c':([28,54,57,83,84,],[55,85,55,55,55,]),'assign_expr':([43,97,],[72,111,]),'class_args':([46,],[74,]),'main_arg':([46,],[75,]),'args':([50,68,],[79,95,]),'arg':([50,68,102,],[80,80,120,]),'var_expr':([61,],[87,]),'sub_args':([100,],[114,]),'necessary_args':([100,],[115,]),'optional_args':([100,127,],[116,139,]),'necessary_arg':([100,127,],[117,140,]),'optional_arg':([100,127,128,],[118,118,141,]),'member_var_name':([107,],[121,]),'trait_decl_stmts':([125,152,],[130,159,]),'trait_decl_stmt':([125,130,152,159,],[131,145,131,145,]),'decl_fn_stmts':([154,],[160,]),'decl_fn_stmt':([154,160,],[161,179,]),'fn_id':([154,156,160,169,],[162,171,162,171,]),'decl_stmts':([155,157,],[164,172,]),'decl_stmt':([155,157,164,172,],[165,165,183,183,]),'var_id':([155,157,164,167,172,209,],[166,166,166,187,166,233,]),'decl_cls_fn_stmts':([156,],[169,]),'decl_cls_fn_stmt':([156,169,],[170,189,]),'decl_static_fn_stmts':([158,],[173,]),'decl_static_fn_stmt':([158,173,],[174,194,]),'static_fn_id':([158,173,],[175,175,]),'vars_id':([167,],[186,]),'pred_args':([180,190,247,253,],[199,211,270,273,]),'main_pred':([180,190,247,253,],[200,200,200,200,]),'type_var_args':([181,191,196,],[202,212,224,]),'type_var_arg':([181,191,196,228,],[203,203,203,248,]),'type_var_id':([181,191,196,228,],[204,204,204,204,]),'next_preds':([195,226,268,],[215,246,281,]),'next_anonymous_necessary_preds':([195,226,268,],[218,218,218,]),'next_anonymous_opt_preds':([195,226,239,268,],[219,219,257,219,]),'next_anonymous_necessary_pred':([195,226,239,268,],[221,221,259,221,]),'next_anonymous_opt_pred':([195,226,239,240,268,276,],[222,222,222,261,222,261,]),'next_named_preds':([241,277,278,301,],[262,289,290,308,]),'next_named_pred':([241,277,278,279,301,],[263,263,263,291,263,]),'next_named_necessary_pred':([241,277,278,279,301,],[264,264,264,264,264,]),'next_named_opt_pred':([241,277,278,279,301,],[265,265,265,265,265,]),'arg_name':([241,277,278,279,301,],[266,266,266,266,266,]),}

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
  ('decl_fn_stmts -> decl_fn_stmts decl_fn_stmt','decl_fn_stmts',2,'p_decl_fn_stmts_r0','parser.py',322),
  ('decl_fn_stmts -> decl_fn_stmt','decl_fn_stmts',1,'p_decl_fn_stmts_r1','parser.py',327),
  ('decl_fn_stmt -> fn_id LP1 pred_args RP1 S_COLON','decl_fn_stmt',5,'p_decl_fn_stmt_r0','parser.py',332),
  ('decl_fn_stmt -> fn_id LP1 pred_args RP1 R_ARROW unary_pred S_COLON','decl_fn_stmt',7,'p_decl_fn_stmt_r1','parser.py',337),
  ('decl_fn_stmt -> fn_id LP3 type_var_args RP3 LP1 pred_args RP1 S_COLON','decl_fn_stmt',8,'p_decl_fn_stmt_r2','parser.py',342),
  ('decl_fn_stmt -> fn_id LP3 type_var_args RP3 LP1 pred_args RP1 R_ARROW unary_pred S_COLON','decl_fn_stmt',10,'p_decl_fn_stmt_r3','parser.py',347),
  ('decl_cls_fn_stmts -> decl_cls_fn_stmts decl_cls_fn_stmt','decl_cls_fn_stmts',2,'p_decl_cls_fn_stmts_r0','parser.py',352),
  ('decl_cls_fn_stmts -> decl_cls_fn_stmt','decl_cls_fn_stmts',1,'p_decl_cls_fn_stmts_r1','parser.py',357),
  ('decl_cls_fn_stmt -> fn_id LP1 pred_args RP1 S_COLON','decl_cls_fn_stmt',5,'p_decl_cls_fn_stmt_r0','parser.py',362),
  ('decl_cls_fn_stmt -> fn_id LP1 pred_args RP1 R_ARROW unary_pred S_COLON','decl_cls_fn_stmt',7,'p_decl_cls_fn_stmt_r1','parser.py',367),
  ('decl_cls_fn_stmt -> fn_id LP3 type_var_args RP3 LP1 pred_args RP1 S_COLON','decl_cls_fn_stmt',8,'p_decl_cls_fn_stmt_r2','parser.py',372),
  ('decl_cls_fn_stmt -> fn_id LP3 type_var_args RP3 LP1 pred_args RP1 R_ARROW unary_pred S_COLON','decl_cls_fn_stmt',10,'p_decl_cls_fn_stmt_r3','parser.py',377),
  ('fn_id -> ID','fn_id',1,'p_fn_id_r0','parser.py',382),
  ('pred_args -> main_pred COMMA next_preds','pred_args',3,'p_pred_args_r0','parser.py',387),
  ('pred_args -> main_pred','pred_args',1,'p_pred_args_r1','parser.py',392),
  ('main_pred -> ID','main_pred',1,'p_main_pred_r0','parser.py',397),
  ('next_preds -> next_anonymous_necessary_preds COMMA next_anonymous_opt_preds COMMA STAR COMMA next_named_preds','next_preds',7,'p_next_preds_r0','parser.py',402),
  ('next_preds -> next_anonymous_necessary_preds COMMA next_anonymous_opt_preds COMMA STAR','next_preds',5,'p_next_preds_r1','parser.py',407),
  ('next_preds -> next_anonymous_necessary_preds COMMA next_anonymous_opt_preds','next_preds',3,'p_next_preds_r2','parser.py',412),
  ('next_preds -> next_anonymous_necessary_preds COMMA STAR COMMA next_named_preds','next_preds',5,'p_next_preds_r3','parser.py',417),
  ('next_preds -> next_anonymous_necessary_preds COMMA STAR','next_preds',3,'p_next_preds_r4','parser.py',422),
  ('next_preds -> next_anonymous_necessary_preds','next_preds',1,'p_next_preds_r5','parser.py',427),
  ('next_preds -> next_anonymous_opt_preds COMMA STAR COMMA next_named_preds','next_preds',5,'p_next_preds_r6','parser.py',432),
  ('next_preds -> next_anonymous_opt_preds COMMA STAR','next_preds',3,'p_next_preds_r7','parser.py',437),
  ('next_preds -> next_anonymous_opt_preds','next_preds',1,'p_next_preds_r8','parser.py',442),
  ('next_preds -> STAR COMMA next_named_preds','next_preds',3,'p_next_preds_r9','parser.py',447),
  ('next_preds -> STAR','next_preds',1,'p_next_preds_r10','parser.py',452),
  ('next_anonymous_necessary_preds -> next_anonymous_necessary_preds COMMA next_anonymous_necessary_pred','next_anonymous_necessary_preds',3,'p_next_anonymous_necessary_preds_r0','parser.py',457),
  ('next_anonymous_necessary_preds -> next_anonymous_necessary_pred','next_anonymous_necessary_preds',1,'p_next_anonymous_necessary_preds_r1','parser.py',462),
  ('next_anonymous_necessary_pred -> unary_pred','next_anonymous_necessary_pred',1,'p_next_anonymous_necessary_pred_r0','parser.py',467),
  ('next_anonymous_opt_preds -> next_anonymous_opt_preds COMMA next_anonymous_opt_pred','next_anonymous_opt_preds',3,'p_next_anonymous_opt_preds_r0','parser.py',472),
  ('next_anonymous_opt_preds -> next_anonymous_opt_pred','next_anonymous_opt_preds',1,'p_next_anonymous_opt_preds_r1','parser.py',477),
  ('next_anonymous_opt_pred -> ASSIGN unary_pred','next_anonymous_opt_pred',2,'p_next_anonymous_opt_pred_r0','parser.py',482),
  ('next_named_preds -> next_named_preds COMMA next_named_pred','next_named_preds',3,'p_next_named_preds_r0','parser.py',487),
  ('next_named_preds -> next_named_pred','next_named_preds',1,'p_next_named_preds_r1','parser.py',492),
  ('next_named_pred -> next_named_necessary_pred','next_named_pred',1,'p_next_named_pred_r0','parser.py',497),
  ('next_named_pred -> next_named_opt_pred','next_named_pred',1,'p_next_named_pred_r1','parser.py',502),
  ('next_named_necessary_pred -> arg_name COLON unary_pred','next_named_necessary_pred',3,'p_next_named_necessary_pred_r0','parser.py',507),
  ('next_named_opt_pred -> arg_name COLON ASSIGN unary_pred','next_named_opt_pred',4,'p_next_named_opt_pred_r0','parser.py',512),
  ('arg_name -> ID','arg_name',1,'p_arg_name_r0','parser.py',517),
  ('type_var_args -> type_var_args COMMA type_var_arg','type_var_args',3,'p_type_var_args_r0','parser.py',522),
  ('type_var_args -> type_var_arg','type_var_args',1,'p_type_var_args_r1','parser.py',527),
  ('type_var_arg -> type_var_id','type_var_arg',1,'p_type_var_arg_r0','parser.py',532),
  ('type_var_arg -> type_var_id COLON unary_pred','type_var_arg',3,'p_type_var_arg_r1','parser.py',537),
  ('type_var_id -> ID','type_var_id',1,'p_type_var_id_r0','parser.py',542),
  ('unary_pred -> pred_name','unary_pred',1,'p_unary_pred_r0','parser.py',547),
  ('unary_pred -> unnamed_pred','unary_pred',1,'p_unary_pred_r1','parser.py',552),
  ('unnamed_pred -> pred_name LP3 args RP3','unnamed_pred',4,'p_unnamed_pred_r0','parser.py',557),
  ('unnamed_pred -> LP3 pred_expr RP3','unnamed_pred',3,'p_unnamed_pred_r1','parser.py',562),
  ('unnamed_pred -> TRAIT_OF LP1 var_expr RP1','unnamed_pred',4,'p_unnamed_pred_r2','parser.py',567),
  ('unnamed_pred -> NONE','unnamed_pred',1,'p_unnamed_pred_r3','parser.py',572),
  ('pred_name -> ID','pred_name',1,'p_pred_name_r0','parser.py',577),
  ('pred_expr -> pred_expr OR pred_expr_a','pred_expr',3,'p_pred_expr_r0','parser.py',582),
  ('pred_expr -> pred_expr_a','pred_expr',1,'p_pred_expr_r1','parser.py',587),
  ('pred_expr_a -> pred_expr_a AND pred_expr_b','pred_expr_a',3,'p_pred_expr_a_r0','parser.py',592),
  ('pred_expr_a -> pred_expr_b','pred_expr_a',1,'p_pred_expr_a_r1','parser.py',597),
  ('pred_expr_b -> NOT pred_expr_c','pred_expr_b',2,'p_pred_expr_b_r0','parser.py',602),
  ('pred_expr_b -> pred_expr_c','pred_expr_b',1,'p_pred_expr_b_r1','parser.py',607),
  ('pred_expr_c -> unary_pred','pred_expr_c',1,'p_pred_expr_c_r0','parser.py',612),
  ('pred_expr_c -> LP1 pred_expr RP1','pred_expr_c',3,'p_pred_expr_c_r1','parser.py',617),
  ('var_expr -> unary_pred DOT member_var_name','var_expr',3,'p_var_expr_r0','parser.py',622),
  ('member_var_name -> ID','member_var_name',1,'p_member_var_name_r0','parser.py',627),
  ('decl_stmts -> decl_stmts decl_stmt','decl_stmts',2,'p_decl_stmts_r0','parser.py',632),
  ('decl_stmts -> decl_stmt','decl_stmts',1,'p_decl_stmts_r1','parser.py',637),
  ('decl_stmt -> var_id S_COLON','decl_stmt',2,'p_decl_stmt_r0','parser.py',642),
  ('decl_stmt -> var_id COLON unary_pred S_COLON','decl_stmt',4,'p_decl_stmt_r1','parser.py',647),
  ('decl_stmt -> LP3 vars_id RP3 S_COLON','decl_stmt',4,'p_decl_stmt_r2','parser.py',652),
  ('decl_stmt -> LP3 vars_id RP3 COLON unary_pred S_COLON','decl_stmt',6,'p_decl_stmt_r3','parser.py',657),
  ('vars_id -> vars_id COMMA var_id','vars_id',3,'p_vars_id_r0','parser.py',662),
  ('vars_id -> var_id','vars_id',1,'p_vars_id_r1','parser.py',667),
  ('var_id -> ID','var_id',1,'p_var_id_r0','parser.py',672),
  ('decl_static_fn_stmts -> decl_static_fn_stmts decl_static_fn_stmt','decl_static_fn_stmts',2,'p_decl_static_fn_stmts_r0','parser.py',677),
  ('decl_static_fn_stmts -> decl_static_fn_stmt','decl_static_fn_stmts',1,'p_decl_static_fn_stmts_r1','parser.py',682),
  ('decl_static_fn_stmt -> static_fn_id LP1 next_preds RP1 S_COLON','decl_static_fn_stmt',5,'p_decl_static_fn_stmt_r0','parser.py',687),
  ('decl_static_fn_stmt -> static_fn_id LP1 next_preds RP1 R_ARROW unary_pred S_COLON','decl_static_fn_stmt',7,'p_decl_static_fn_stmt_r1','parser.py',692),
  ('decl_static_fn_stmt -> static_fn_id LP3 type_var_args RP3 LP1 next_preds RP1 S_COLON','decl_static_fn_stmt',8,'p_decl_static_fn_stmt_r2','parser.py',697),
  ('decl_static_fn_stmt -> static_fn_id LP3 type_var_args RP3 LP1 next_preds RP1 R_ARROW unary_pred S_COLON','decl_static_fn_stmt',10,'p_decl_static_fn_stmt_r3','parser.py',702),
  ('decl_static_fn_stmt -> static_fn_id LP1 RP1 S_COLON','decl_static_fn_stmt',4,'p_decl_static_fn_stmt_r4','parser.py',707),
  ('decl_static_fn_stmt -> static_fn_id LP1 RP1 R_ARROW unary_pred S_COLON','decl_static_fn_stmt',6,'p_decl_static_fn_stmt_r5','parser.py',712),
  ('decl_static_fn_stmt -> static_fn_id LP3 type_var_args RP3 LP1 RP1 S_COLON','decl_static_fn_stmt',7,'p_decl_static_fn_stmt_r6','parser.py',717),
  ('decl_static_fn_stmt -> static_fn_id LP3 type_var_args RP3 LP1 RP1 R_ARROW unary_pred S_COLON','decl_static_fn_stmt',9,'p_decl_static_fn_stmt_r7','parser.py',722),
  ('static_fn_id -> ID','static_fn_id',1,'p_static_fn_id_r0','parser.py',727),
  ('print_stmt -> PRINTINFO to_print S_COLON','print_stmt',3,'p_print_stmt_r0','parser.py',732),
  ('generate_stmt -> GENERATE to_print S_COLON','generate_stmt',3,'p_generate_stmt_r0','parser.py',737),
  ('to_print -> ID','to_print',1,'p_to_print_r0','parser.py',742),
  ('to_print -> boolean_expr','to_print',1,'p_to_print_r1','parser.py',747),
  ('to_print -> unnamed_pred','to_print',1,'p_to_print_r2','parser.py',752),
  ('boolean_expr -> boolean_expr OR boolean_expr_a','boolean_expr',3,'p_boolean_expr_r0','parser.py',757),
  ('boolean_expr -> boolean_expr_a','boolean_expr',1,'p_boolean_expr_r1','parser.py',762),
  ('boolean_expr_a -> boolean_expr_a XOR boolean_expr_b','boolean_expr_a',3,'p_boolean_expr_a_r0','parser.py',767),
  ('boolean_expr_a -> boolean_expr_b','boolean_expr_a',1,'p_boolean_expr_a_r1','parser.py',772),
  ('boolean_expr_b -> boolean_expr_b AND boolean_expr_c','boolean_expr_b',3,'p_boolean_expr_b_r0','parser.py',777),
  ('boolean_expr_b -> boolean_expr_c','boolean_expr_b',1,'p_boolean_expr_b_r1','parser.py',782),
  ('boolean_expr_c -> boolean_expr_c EQ boolean_expr_d','boolean_expr_c',3,'p_boolean_expr_c_r0','parser.py',787),
  ('boolean_expr_c -> boolean_expr_c NEQ boolean_expr_d','boolean_expr_c',3,'p_boolean_expr_c_r1','parser.py',792),
  ('boolean_expr_c -> boolean_expr_d','boolean_expr_c',1,'p_boolean_expr_c_r2','parser.py',797),
  ('boolean_expr_d -> NOT boolean_expr_e','boolean_expr_d',2,'p_boolean_expr_d_r0','parser.py',802),
  ('boolean_expr_d -> boolean_expr_e','boolean_expr_d',1,'p_boolean_expr_d_r1','parser.py',807),
  ('boolean_expr_e -> atomic_boolean_expr','boolean_expr_e',1,'p_boolean_expr_e_r0','parser.py',812),
  ('boolean_expr_e -> LP1 boolean_expr RP1','boolean_expr_e',3,'p_boolean_expr_e_r1','parser.py',817),
  ('atomic_boolean_expr -> constants','atomic_boolean_expr',1,'p_atomic_boolean_expr_r0','parser.py',822),
  ('atomic_boolean_expr -> unary_pred LP1 args RP1','atomic_boolean_expr',4,'p_atomic_boolean_expr_r1','parser.py',827),
  ('atomic_boolean_expr -> unary_pred IMPLIES unary_pred','atomic_boolean_expr',3,'p_atomic_boolean_expr_r2','parser.py',832),
  ('atomic_boolean_expr -> LP1 unary_pred EQ unary_pred RP1','atomic_boolean_expr',5,'p_atomic_boolean_expr_r3','parser.py',837),
  ('atomic_boolean_expr -> LP1 unary_pred NEQ unary_pred RP1','atomic_boolean_expr',5,'p_atomic_boolean_expr_r4','parser.py',842),
  ('constants -> TRUE','constants',1,'p_constants_r0','parser.py',847),
  ('constants -> FALSE','constants',1,'p_constants_r1','parser.py',852),
  ('args -> args COMMA arg','args',3,'p_args_r0','parser.py',857),
  ('args -> arg','args',1,'p_args_r1','parser.py',862),
  ('arg -> ID','arg',1,'p_arg_r0','parser.py',867),
  ('assign_stmt -> names ASSIGN assign_expr S_COLON','assign_stmt',4,'p_assign_stmt_r0','parser.py',872),
  ('names -> names COMMA name','names',3,'p_names_r0','parser.py',877),
  ('names -> name','names',1,'p_names_r1','parser.py',882),
  ('name -> ID','name',1,'p_name_r0','parser.py',887),
  ('assign_expr -> names ASSIGN assign_expr','assign_expr',3,'p_assign_expr_r0','parser.py',892),
  ('assign_expr -> names','assign_expr',1,'p_assign_expr_r1','parser.py',897),
]
