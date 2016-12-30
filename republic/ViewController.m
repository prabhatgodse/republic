//
//  ViewController.m
//  republic
//
//  Created by Prabhat Godse on 12/3/16.
//  Copyright © 2016 Prabhat Godse. All rights reserved.
//

#import "ViewController.h"

@interface ViewController () <UITableViewDelegate, UITableViewDataSource> {
    UILabel *label;
    UITableView *yourReprList;
}

@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view, typically from a nib.
    self.view.backgroundColor = [UIColor colorWithWhite:0.8 alpha:1.0];
    label = [[UILabel alloc] initWithFrame:CGRectMake(10, 10, 250, 50)];
    [label setText:@"Knwo your representative"];
    [self.view addSubview:label];
    
    yourReprList = [[UITableView alloc] init];
    yourReprList.delegate = self;
    yourReprList.dataSource = self;
    [yourReprList registerClass:[UITableViewCell class] forCellReuseIdentifier:@"resue"];
    [yourReprList reloadData];
}


- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

- (void)viewDidAppear:(BOOL)animated {
    [super viewDidAppear:animated];
    
    CGFloat height = self.view.frame.size.height - label.frame.size.height;
    yourReprList.frame = CGRectMake(0, 10, self.view.frame.size.width, height);
}

- (NSInteger)numberOfSectionsInTableView:(UITableView *)tableView {
    return 1;
}

- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section {
    // mayor + congress man + 2- senator + governor + president
    return 5;
}

- (UITableViewCell*)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath {
    UITableViewCell *cell;
    
    return cell;
}

@end
