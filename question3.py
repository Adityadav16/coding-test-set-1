transition_table = {
    State.UNAUTHORIZED: [
        (Action.LOGIN, login_checker, State.AUTHORIZED)
    ],

    State.AUTHORIZED: [
        (Action.LOGOUT, logout_checker, State.UNAUTHORIZED),
        (Action.DEPOSIT, deposit_checker, State.AUTHORIZED),
        (Action.WITHDRAW, withdraw_checker, State.AUTHORIZED),
        (Action.BALANCE, balance_checker, State.AUTHORIZED)
    ]
}
