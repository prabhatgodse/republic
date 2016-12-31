//
//  ViewController.m
//  republic
//
//  Created by Prabhat Godse on 12/3/16.
//  Copyright © 2016 Prabhat Godse. All rights reserved.
//

#import "ViewController.h"

#import <IGListKit/IGListKit.h>
#import "HomeFeedSectionController.h"

@interface ViewController () <UITableViewDelegate, UITableViewDataSource, IGListAdapterDelegate> {
    UILabel *label;
    IGListCollectionView *collectionView;
}
@property (nonatomic, strong) IGListAdapter *adapter;
@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view, typically from a nib.
    self.view.backgroundColor = [UIColor colorWithWhite:0.8 alpha:1.0];
    label = [[UILabel alloc] initWithFrame:CGRectMake(10, 10, 250, 50)];
    [label setText:@"Know your representative"];
    [self.view addSubview:label];
    
    
    UICollectionViewFlowLayout *layout = [[UICollectionViewFlowLayout alloc] init];
    
    collectionView = [[IGListCollectionView alloc] initWithFrame:CGRectZero
                                            collectionViewLayout:layout];
    [self.view addSubview:collectionView];
    
    _adapter = [[IGListAdapter alloc] initWithUpdater:[[IGListAdapterUpdater alloc] init]
                                       viewController:self
                                     workingRangeSize:0];
    _adapter.collectionView = collectionView;
    _adapter.dataSource = self;
}


- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

- (void)viewDidAppear:(BOOL)animated {
    [super viewDidAppear:animated];
}

- (void)viewDidLayoutSubviews {
    [super viewDidLayoutSubviews];
    CGFloat height = self.view.frame.size.height - label.frame.size.height;
    collectionView.frame = CGRectMake(0, 10, self.view.frame.size.width, height);
    [self.adapter performUpdatesAnimated:YES completion:nil];
}


#pragma mark IGListAdapterDataSource

- (NSArray<id <IGListDiffable>> *)objectsForListAdapter:(IGListAdapter *)listAdapter {
    return @[@"Donald Trump", @"Small hands"];
    
}

- (IGListSectionController <IGListSectionType> *)listAdapter:(IGListAdapter *)listAdapter
                                  sectionControllerForObject:(id)object {
    return [[HomeFeedSectionController alloc] init];
}

- (nullable UIView *)emptyViewForListAdapter:(IGListAdapter *)listAdapter {
    return nil;
}

@end
