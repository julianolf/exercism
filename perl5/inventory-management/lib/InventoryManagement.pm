package InventoryManagement;

use v5.38;

sub create_inventory ($items) {
    return add_items({}, $items);
}

sub add_items ( $inventory, $items ) {
    $$inventory{$_}++ for @$items;
    return $inventory;
}

sub remove_items ( $inventory, $items ) {
    for my $item (@$items) {
        if ($$inventory{$item} > 0) {
            $$inventory{$item}--;
        }
    }
    return $inventory;
}

sub delete_item ( $inventory, $item ) {
    delete $$inventory{$item};
    return $inventory;
}
